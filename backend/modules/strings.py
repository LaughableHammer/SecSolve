import sh


def run(filepath):
    try:
        result = sh.strings(filepath)
        return {
            "module": "strings",
            "success": True,
            "output": result,
        }

    except sh.ErrorReturnCode as e:
        return {
            "module": "strings",
            "success": False,
            "output": f"Command {e.full_cmd} exited with {e.exit_code}",
        }
