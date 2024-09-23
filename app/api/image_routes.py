from flask import Blueprint, request, redirect
from app.forms.comment_form import CommentForm
from app.models import db, Image, Label, Comment, Favorite, Stash
from app.models.tables import label_image_table
from flask_login import current_user, login_required
from app.api.s3_helper import (
    upload_file_to_s3, get_unique_filename)
from app.forms.image_form import ImageForm
from app.forms.image_update_form import ImageUpdateForm



image_routes = Blueprint("images", __name__)

def format_errors(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = dict()

    for field in validation_errors:
        errorMessages[field] = [error for error in validation_errors[field]]

    return errorMessages

# Basic Implementation, for production should only display images the current user hasn't already saved to a
# stash, if user is not logged in then it should display any images. Also need to set a limit to how many images
# to display on home page
@image_routes.route("")
def get_images():
    """
    Gets all Images in database and returns a list of basic image details
    """
    images = Image.query.all()
    return {'images': [image.to_dict_basic() for image in images]}


@image_routes.route("/<int:id>")
@login_required
def get_specific_image(id):
    """
    Gets the image with the specified ID and returns a list of complete image details
    """
    image = Image.query.get(id)

    #! If image does not exist
    if not image:
        return {"errors": "Image not found"}, 404

    return image.to_dict()


@image_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
    """
    Uploads image to AWS bucket and creates new image in db
    """
    form = ImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        # print(current_user.to_dict(), file=sys.stdout)

        if "url" not in upload:
            # if the dictionary doesn't have a url key
            # it means that there was an error when you tried to upload
            # so you send back that error message (and you printed it above)
            print("Url not in upload")
            return format_errors(form.errors)

        url = upload["url"]
        new_image = Image(
            user_id=current_user.id,
            url=url,
            title=form.data["title"],
            description=form.data["description"],
        )

        labels = form.data["labels"]

        if labels != "":
            # Checking to see if there are any labels
            # TODO: When adding ", " when typing, label name now starts with " "
            labels = labels.split(",")
            # Splitting csv values into a list for iteration
            for label in labels:
                # Iterating through list to add labels
                lower_label = label.lower()
                find_label = Label.query.filter(Label.name == lower_label).one_or_none()
                # Checking to see if label has already been created
                if not find_label:
                    # If there are no labels that match then create a new label and add it, then make the association on the
                    # label_images table for the new image for each label that is new
                    new_label = Label(name=lower_label)
                    new_image.labels.append(new_label)
                    db.session.add(new_label)
                else:
                    # If the label already exists just add that label we found to the new image on the label_image table
                    new_image.labels.append(find_label)

        else:
            # If no labels were given then simply add the image
            db.session.add(new_image)

        db.session.commit()

        return new_image.to_dict()

    if form.errors:
        return format_errors(form.errors)

    return


@image_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_specific_image(id):
    """
    Updates the image with the specified ID
    """
    form = ImageUpdateForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    image = Image.query.get(id)
    labels = form.data['labels']

    if not image:
        return {"errors": "Images not found"}, 404

    if image.user_id != current_user.id:
        return {"errors": "This is not your image"}, 500


    #? LABEL UPDATES AS WELL
    if labels != '':
        # Checking to see if there are any labels
        lbl_lst = labels.split(',')
        # Splitting csv values into a list for iteration
        for label in lbl_lst:
            # Iterating through list to add labels
            lower_label = label.lower()
            find_label = Label.query.filter(Label.name == lower_label).one_or_none()
            # Checking to see if label has already been created
            if not find_label:
            # If there are no labels that match then create a new label and add it, then make the association on the
            # label_images table for the new image for each label that is new
                new_label = Label(name = lower_label)
                image.labels.append(new_label)
                db.session.add(new_label)
            else:
            # If the label already exists just add that label we found to the new image on the label_image table
                image.labels.append(find_label)
                
    if form.validate_on_submit():
        image.title = form.data['title']
        image.description = form.data['description']
        # TODO: Update label instead of having to delete manually?
        db.session.commit()
        return image.to_dict()

    return format_errors(form.errors), 400


@image_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_image(id):
    """
    Delete image by id
    """
    image_to_delete = Image.query.get(id)
    
    if not image_to_delete:
        return {"errors": "Image not found"}

    if image_to_delete.user_id != current_user.id:
        return {"errors": "This is not your image"}, 500

    #? Delete from db but maybe not from bucket
    db.session.delete(image_to_delete)
    db.session.commit()

    return {"message": "Successfully Deleted"}


#! Comments
@image_routes.route("/<int:id>/new_comment", methods=["POST"])
@login_required
def post_new_comment(id):
    """
    User can post new comments
    """
    form = CommentForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        comment = form.data["comment"]
        new_comment = Comment(
            user_id=current_user.id, image_id=id, comment=comment
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.to_dict_basic()

    if form.errors:
        return format_errors(form.errors)


#! Favorites
@image_routes.route("/<int:id>/favorite", methods=["POST"])
@login_required
def favorite_an_image(id):
    img = Image.query.get(id)
    fav_img = Favorite(
        image_id = id,
        user_id = current_user.id
    )

    if not img:
        return {"errors": "Image not found"}, 404


    
    # ! Run a query for unique to avoid doubling a favorite
    favorites = Favorite.query.filter(Favorite.user_id == current_user.id).all()
    q = [fav for fav in favorites if fav.image_id == fav_img.image_id and fav.user_id == fav_img.user_id]
    if q:
        return {"errors": "Favorite Already Exists"}, 400

    # ! ELSE commit to users favorites list
    db.session.add(fav_img)
    db.session.commit()
    return img.to_dict()


# ! Stash an Image
@image_routes.route("/<int:id>/stashes/<int:stashId>", methods=["POST"])
@login_required
def stash_an_image(id, stashId):
    stash = Stash.query.get(stashId)
    if not stash:
        return {"errors": "Stash not found"}
    elif stash.user_id != current_user.id:
        return {"errors": "This stash is not yours"}, 500
    else:
        image = Image.query.get(id)
        if not image:
            return {"errors": "Image not Found"}

        for img in stash.images:
            if img.id == id:
                return {"errors": "Image already stashed here"}, 500
        
        stash.images.append(image)
        db.session.commit()

        return stash.to_dict()


# ! LABEL MANIPULATION ROUTES

# DELETE api/images/:imageId/label/:labelId
@image_routes.route("/<int:id>/label/<string:labelName>", methods=["DELETE"])
@login_required
def del_label(id, labelName):
    img = Image.query.get(id)
    
    if not img:
        return {"errors": "Image not found"}

    for lbl in img.labels:
        if lbl.name == labelName:
            img.labels.remove(lbl)
            db.session.commit()
            return img.to_dict()
        
    return {"errors": "Label not Found"}, 404



# ! SEARCH FEATURE

# GET api/images/:labelname
@image_routes.route("/<string:labelName>")
def find_by_label(labelName):
    images = Image.query.all()
    res = []
    for image in images:
        for label in image.labels:
            if label.name == labelName:
                res.append(image.to_dict_basic())

    return {"images": res}

