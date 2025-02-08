from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from file_processing import process_file
from forms import UploadFileForm
from config import Config


def register_routes(app):
    """Register Flask routes."""

    @app.route("/", methods=["GET", "POST"])
    def home():
        form = UploadFileForm()
        if form.validate_on_submit():
            file = form.file.data
            filename = secure_filename(file.filename)
            file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
            file.save(file_path)

            result = process_file(file_path, filename)
            return jsonify(result)  # Return JSON response

        return render_template("index.html", form=form)
