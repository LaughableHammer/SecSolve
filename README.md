# SecSolve

An all-in-one forensics tool for CTF competitions.

## Features
- Upload and analyze files using various forensic techniques.
- Supports multiple modules that run different CTF-related tools.
- Provides structured JSON output with results from each module.
- Built with Flask and Python.

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/SecSolve.git
cd SecSolve/backend
```

### **2. Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r Requirements.txt
```

### **4. Run the Application**
```bash
python app.py
```
By default, the application runs on `http://127.0.0.1:5000/`.

---

## **Project Structure**
```
SecSolve/
├── backend/
│   ├── app.py                # Main Flask application
│   ├── modules/              # Directory for analysis modules
│   │   ├── __init__.py       # Init file for module discovery
│   │   ├── module.py         # Example module
│   ├── static/
│   │   ├── files/            # Uploaded files are stored here
│   │   ├── test_files/       # Files used during testing are stored here
│   ├── tests/                # Unit tests for the application
│   │   ├── test_data/        # Sample test files are stored here
│   │   ├── test_app.py       # Tests for the main app
│   │   ├── test_module.py    # Example test for a module
│   ├── templates/            # HTML templates for rendering pages
│   │   ├── index.html        # Main frontend page
│   ├── forms.py              # WTForms definitions for file upload
│   ├── config.py             # Configuration settings
│   ├── modules_loader.py     # Dynamically loads all added modules
│   ├── file_processing.py    # Logic for running individual modules on the input file
│   ├── routes.py             # All application routes
│   ├── Requirements.txt      # Project dependencies
│   ├── README.md             # Project documentation
│   ├── .gitignore            # Files that shouldn't be pushed to Git
```

---

## **Developing Locally**

### **Adding a New Module**
1. Create a new Python file inside the `modules/` directory labelled with the feature it is implementing, e.g., `modules/strings.py`.
2. Define a `run(filepath)` function that processes the file and returns a dictionary.
   ```python
   import sh


    def run(filepath):
        try:
            result = sh.strings(filepath)
            return {
                "module": "strings",
                "success": "True",
                "output": result,
            }

        except sh.ErrorReturnCode as e:
            return {
                "module": "strings",
                "success": "False",
                "output": f"Command {e.full_cmd} exited with {e.exit_code}",
            }
   ```
3. The new module will automatically be discovered when the app runs.

---

## **Running Tests**
Ensure you have `pytest` installed:
```bash
pip install pytest
```

### **Run All Tests**
```bash
pytest
```

### **Run a Specific Test File**
```bash
pytest tests/test_app.py
```

### **Run a Specific Test Case**
```bash
pytest tests/test_app.py -k "test_home_page"
```

### **See debugging print statements and which tests are passing/failing**
```bash
pytest -s -v
```

---

## **Troubleshooting**

### **Common Issues & Fixes**
- **ModuleNotFoundError**: Run `export PYTHONPATH=.` in the `/backend` folder before running `pytest`.
- **Port Already in Use**: If `5000` is occupied, modify the port in the app.py file `app.run(host="127.0.0.1", port="5001", debug=True)`.
