from flask import Blueprint, redirect, render_template, request
from app.models import db, Image
from app.forms import ImageForm
from flask_login import current_user, login_required
from app.api.boto import upload_file_to_s3, get_unique_filename

image_routes = Blueprint("images", __name__)


@image_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
    form = ImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
            # if the dictionary doesn't have a url key
            # it means that there was an error when you tried to upload
            # so you send back that error message (and you printed it above)
            return render_template("post_form.html", form=form, errors=[upload])

        url = upload["url"]
        new_image = Image(image=url)
        db.session.add(new_image)
        db.session.commit()
        return new_image

    if form.errors:
        print(form.errors)
        return form.errors

    return 
