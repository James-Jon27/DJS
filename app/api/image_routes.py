from flask import Blueprint, request, redirect
from app.models import db, Image
from flask_login import current_user, login_required
from app.api.s3_helper import (
    upload_file_to_s3, get_unique_filename)
from app.forms.image_form import ImageForm
# import sys



image_routes = Blueprint("images", __name__)



@image_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
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
        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict_basic()

    if form.errors:
        return form.errors

    return