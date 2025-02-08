import os
import logging
from modules_loader import load_modules

modules = load_modules()


def process_file(filepath, filename):
    """Process uploaded file using available modules."""
    if not os.path.exists(filepath):
        logging.error(f"File {filepath} not found.")
        return {"status": "Error", "message": "File not found."}

    file_size = os.path.getsize(filepath)
    results = []

    for module_name, module in modules.items():
        try:
            result = module.run(filepath)
            results.append(result)
        except Exception as e:
            logging.error(f"Error running module '{module_name}': {e}")
            results.append({"module": module_name, "error": str(e)})

    return {
        "status": "File processed successfully.",
        "filename": filename,
        "file_size": file_size,
        "results": results,
    }
