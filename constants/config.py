import os

def getFolder():
    """Return the folder where the files are"""
    current_dir = os.path.dirname(__file__)  # Get to .../project/constants
    project_root = os.path.abspath(os.path.join(current_dir, os.pardir))  # Get to .../project
    return os.path.join(project_root, "files") # Get to .../project/files


def getClasses():
    """Return a list of the txt files located in the project"""

    CLASSES = []

    # list the files located in the path
    for file in os.listdir(getFolder()):
        # if the file is a txt file
        if file.endswith(".txt"):
            # we take the name of the file 
            CLASSES.append(os.path.splitext(file)[0])

    return CLASSES



MODES = {
    "NATIVE": "Native",
    "NON NATIVE": "Non Native",
    "MIXED": "Mixed"
}

CLASSES = getClasses()
SELECTED_CLASSES = ""

