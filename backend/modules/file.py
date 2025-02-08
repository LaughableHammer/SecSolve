import sh


def run(filepath):
    try:
        result = sh.file(filepath)
        return {
            "module": "file",
            "success": True,
            "output": result,
        }

    except sh.ErrorReturnCode as e:
        return {
            "module": "file",
            "success": False,
            "output": f"Command {e.full_cmd} exited with {e.exit_code}",
        }
