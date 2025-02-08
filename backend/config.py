import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mykeythatiwillreplaceprobably")
    MAX_CONTENT_LENGTH = 32 * 1000 * 1000  # 32MB max file upload size
    UPLOAD_FOLDER = "static/files"
    MODULES_DIR = "modules"
