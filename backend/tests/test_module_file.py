import os
from modules.file import run


def test_file():
    test_file_path = "tests/test_data/sample.txt"
    os.makedirs("tests/test_data", exist_ok=True)

    with open(test_file_path, "w") as f:
        f.write("Sample content for testing.")

    result = run(test_file_path)

    assert result is not None
    assert result["module"] == "file"
    assert result["success"]
    assert (
        result["output"]
        == "tests/test_data/sample.txt: ASCII text, with no line terminators\n"
    )

    # Clean up
    os.remove(test_file_path)
