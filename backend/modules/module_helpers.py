import shutil


def is_available(program):
    """Checks if a particular tool is available on the server

    Args:
        program (string): the tool to search for

    Returns:
        boolean: True if it exists, otherwise False
    """
    return shutil.which(program) is not None
