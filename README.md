# Project Deployment Instructions

## Prerequisites

1. **Git preinstalled and configured**
2. **Python 3.10+ must be installed on the target machine**

## Steps

1. Navigate to a directory to hold the project.
2. Open a browser and navigate to https://github.com/reywald/risevest_test_app
3. Download the repository and copy it to the directory in step (1).
4. Extract the contents to the directory.
5. Navigate into the newly extracted repository.
6. Open a command-line interface (CLI) and navigate to the repository's directory.
7. Create a directory called **.venv** to contain the virtual environment for python.
   - **_mkdir .venv_**
8. Install **pipenv**:
   - **_python -m pip install pipenv_** or **_pip install pipenv_**.
9. Once completed, create the virtual environment and install all dependencies in one go:
   - **_pipenv install_**
10. Start up the virtual environment:
    - **_pipenv shell_** 👍
11. Run the tests:
    - **_python main.py_**.
12. The test suite will randomly select a browser driver (Chrome, Edge, Firefox), automatically download it and run the tests
