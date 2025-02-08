from flask import Flask
from config import Config
from routes import register_routes
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Register Routes
register_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
