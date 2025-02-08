import os
import importlib
import logging
from config import Config


def load_modules():
    """Dynamically load modules from the modules directory."""
    EXCLUDED_FILES = {"__init__.py", "module_helpers.py"}

    modules = {}
    if not os.path.exists(Config.MODULES_DIR):
        logging.warning(f"Modules directory '{Config.MODULES_DIR}' does not exist.")
        return modules  # Return empty dict if no modules folder

    for filename in os.listdir(Config.MODULES_DIR):
        if filename.endswith(".py") and filename not in EXCLUDED_FILES:
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f"{Config.MODULES_DIR}.{module_name}")
                modules[module_name] = module
            except Exception as e:
                logging.error(f"Failed to load module {module_name}: {e}")

    return modules
