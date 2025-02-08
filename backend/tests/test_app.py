import os
import pytest
from app import app


@pytest.fixture  # provides context for the application for testing
def client():
    app.config["TESTING"] = True
    app.config["UPLOAD_FOLDER"] = "static/test_files"
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    yield app.test_client()
    # Clean up test files after tests
    for f in os.listdir(app.config["UPLOAD_FOLDER"]):
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], f))


# Test the home page
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Submit" in response.data


# Test file upload and processing
def test_file_upload(client):
    test_file_path = "tests/test_data/sample.txt"
    os.makedirs("tests/test_data", exist_ok=True)

    with open(test_file_path, "w") as f:
        f.write("This is a test file.")

    with open(test_file_path, "rb") as test_file:
        response = client.post(
            "/", data={"file": test_file}, content_type="multipart/form-data"
        )

    assert response.status_code == 200

    os.remove(test_file_path)
