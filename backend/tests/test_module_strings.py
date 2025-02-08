import os
from modules.strings import run


def test_strings():
    test_file_path = "tests/test_data/sample.txt"
    os.makedirs("tests/test_data", exist_ok=True)

    with open(test_file_path, "w") as f:
        f.write("Sample content for testing.")

    result = run(test_file_path)

    assert result is not None
    assert result["module"] == "strings"
    assert result["success"]
    assert result["output"] == "Sample content for testing.\n"

    # Clean up
    os.remove(test_file_path)


# TODO: Negative case if one exists for strings.
