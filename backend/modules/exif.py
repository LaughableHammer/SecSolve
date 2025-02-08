import sh
from modules import module_helpers


def run(filepath):
    if not module_helpers.is_available("exiftool"):
        return {
            "module": "exiftool",
            "success": False,
            "output": "exiftool is not installed",
        }

    try:
        result = sh.exiftool(filepath)
        return {
            "module": "exiftool",
            "success": True,
            "output": result,  # result.stdout.decode(),
        }
    except sh.ErrorReturnCode as e:
        return {
            "module": "exiftool",
            "success": False,
            "output": f"Command {e.full_cmd} exited with {e.exit_code}",
        }
