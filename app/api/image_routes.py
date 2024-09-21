from flask import Blueprint, request, redirect
from app.models import db, Image, Label
from app.models.tables import label_image_table
from flask_login import current_user, login_required
from app.api.s3_helper import (
    upload_file_to_s3, get_unique_filename)
from app.forms.image_form import ImageForm
from app.forms.image_update_form import ImageUpdateForm
import sys



image_routes = Blueprint("images", __name__)

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
def get_specific_image(id):
    """
    Gets the image with the specified ID and returns a list of complete image details
    """
    image = Image.query.get(id)
    return image.to_dict()

@image_routes.route("/<int:id>")
def update_specific_image(id):
    """
    Updates the image with the specified ID
    """
    form = ImageUpdateForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        image = Image.query.get(id)
        image.title = form.data["title"],
        image.description = form.data["description"]
        db.session.commit()
        return image.to_dict()

    return form.errors, 400

    

@image_routes.route("/<int:id>/images")
def get_user_images(id):
    """
    Gets all the images posted by the specified user
    """
    images = Image.query.filter(Image.id == id).all()
    return {'images': [image.to_dict_basic() for image in images]}


@image_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
    """
    Uploads image to AWS bucket and creates new image in db
    """
    form = ImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        # print(current_user.to_dict(), file=sys.stdout)


        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            print('Url not in upload')
            return form.errors

        url = upload["url"]
        new_image = Image(
            user_id = current_user.id,
            url = url,
            title = form.data["title"],
            description = form.data["description"]
            )

        labels = form.data['labels']

        if labels != '':
        # Checking to see if there are any labels
            labels = labels.split(',')
            # Splitting csv values into a list for iteration
            for label in labels:
            # Iterating through list to add labels
                lower_label = label.lower()
                find_label = Label.query.filter(Label.name == lower_label).one_or_none()
                # Checking to see if label has already been created
                if find_label is None:
                # If there are no labels that match then create a new label and add it, then make the association on the
                # label_images table for the new image for each label that is new
                    new_label = Label(name = lower_label)
                    new_image.labels.append(new_label)
                    db.session.add(new_label)
                else:
                # If the label already exists just add that label we found to the new image on the label_image table
                    new_image.labels.append(find_label)
                
        else:
        # If no labels were given then simply add the image
            db.session.add(new_image)

        db.session.commit()
            
        return new_image.to_dict_basic()

    if form.errors:
        return form.errors

    return

