import random
import os

def getFolder():
    """Return the folder where the code is"""

    return os.path.join(os.path.dirname(__file__), "files")

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

def getSelectedFile():
    """Return the file selected by the user"""

    CLASSES = getClasses()

    # meanwhile the user selects the file
    while(True):
        print("Select between these files to study: ")
        for classe in CLASSES:
            print(classe)
        selected_file = input()

        if selected_file in CLASSES:
            return (f"{getFolder()}/{selected_file}.txt")
        else:
            print("Error: file doesn't exist\n")


def main():
    """Main Code"""

    selected_file = getSelectedFile()
    try:
        with open(selected_file) as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: file doesn't exist")
    

if __name__ == '__main__':
    main()