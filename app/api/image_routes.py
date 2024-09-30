from flask import Blueprint, request, redirect
from  sqlalchemy.sql.expression import func
from app.forms.comment_form import CommentForm
from app.models import db, Image, Label, Comment, Favorite, Stash
from app.models.tables import label_image_table
from flask_login import current_user, login_required
from app.api.s3_helper import (
    upload_file_to_s3, get_unique_filename, remove_file_from_s3)
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
#! TODO - Also filter out images that user has already stashed
@image_routes.route("")
def get_images():
    """
    Gets all Images in database and returns a list of basic image details
    """
    if(current_user.is_anonymous):
        images = Image.query.order_by(func.random()).limit(20).all()
    else:
        images = Image.query.order_by(func.random()).filter(Image.user_id != current_user.id).limit(20).all()
    
    image_holder = {}
    for image in images:
        image_holder[image.id] = image.to_dict()
    return image_holder


@image_routes.route("/<int:id>")
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
        print(upload)
        # print(current_user.to_dict(), file=sys.stdout)

        if "url" not in upload:
            # if the dictionary doesn't have a url key
            # it means that there was an error when you tried to upload
            # so you send back that error message (and you printed it above)
            print("Url not in upload")
            return format_errors(form.errors)

        desc = form.data["description"]
        if desc == '':
            desc = None


        url = upload["url"]
        new_image = Image(
            user_id=current_user.id,
            url=url,
            title=form.data["title"],
            description=desc,
        )

        labels = form.data["labels"]

        if labels != "":
        # Checking to see if there are any labels
            create_labels(labels, new_image)
            
        else:
            # If no labels were given then simply add the image
            db.session.add(new_image)

        db.session.commit()

        return new_image.to_dict()

    if form.errors:
        return {"errors": format_errors(form.errors)}, 400

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

                
    if form.validate_on_submit():
        image.title = form.data['title']
        image.description = form.data['description']


        image_label = Label.query.filter(Label.images.any(id = id)).all()
        # Finding all labels associated with a specific image id
        for label in image_label:
            # For every label, remove the association with the specified image
            old_label = Label.query.get(label.id)
            image.labels.remove(old_label)
        
        if labels != "":
            create_labels(labels, image)
        # Call function to create new labels

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

    remove_file_from_s3(image_to_delete.url)
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
        return new_comment.to_dict()

    if form.errors:
        return {"errors" : format_errors(form.errors)}, 400
    
@image_routes.route("/<int:id>/comments")
def getImageComments(id):
    """
    Get comments on image by id
    """
    comments = Comment.query.filter(Comment.image_id == id).all()
    
    comment_holder = {}
    for comment in comments:
        comment_holder[comment.id] = comment.to_dict()
    return comment_holder



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

        if image in stash.images:
            return {"errors": "Image already stashed here"}, 500
        
        stash.images.append(image)
        db.session.commit()

        return stash.to_dict()


#! Un-Stash an Image
@image_routes.route("/<int:id>/stashes/<int:stashId>", methods=["DELETE"])
@login_required
def un_stash_an_image(id, stashId):
    stash = Stash.query.get(stashId)
    if not stash:
        return {"errors": "Stash not found"}
    elif stash.user_id != current_user.id:
        return {"errors": "This stash is not yours"}, 500
    else:
        image = Image.query.get(id)
        if not image:
            return {"errors": "Image not Found"}

        if image in stash.images:
            stash.images.remove(image)

        db.session.commit()

        return stash.to_dict()


# ! LABEL MANIPULATION ROUTES

# DELETE api/images/:imageId/label/:labelId
@image_routes.route("/labels")
def get_label():
    """
    Query for all labels returns them in a list
    """
    # labels = Label.query.order_by(func.random()).limit(10).all()
    labels = Label.query.all()

    label_holder = {}
    for label in labels:
        label_holder[label.id] = label.to_dict_basic()
    
    return label_holder



# ! SEARCH FEATURE

# GET api/images/:labelname
@image_routes.route("/<string:labelName>")
def find_by_label(labelName):
    images = Image.query.all()
    res = {}
    for image in images:
        for label in image.labels:
            if label.name == labelName:
                res[image.id] = image.to_dict()

    return res

def create_labels(labels, image):
    labels = labels.strip()
    if(labels.endswith(',')):
            labels = labels[:-1]
    labels = labels.split(',')
    for i, label in enumerate(labels):
        labels[i] = label.strip()
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
            image.labels.append(new_label)
            db.session.add(new_label)
        else:
            # If the label already exists just add that label we found to the new image on the label_image table
            image.labels.append(find_label)
