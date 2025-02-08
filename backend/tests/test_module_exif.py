import os
from modules.exif import run


def test_exit():
    test_file_path = "tests/test_data/sample.txt"
    os.makedirs("tests/test_data", exist_ok=True)

    with open(test_file_path, "w") as f:
        f.write("Sample content for testing.")

    result = run(test_file_path)

    assert result is not None
    assert result["module"] == "exiftool"
    assert result["success"]
    assert "ExifTool Version Number" in result["output"]

    # Clean up
    os.remove(test_file_path)
