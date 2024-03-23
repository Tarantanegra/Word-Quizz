import json
import random
import os

CLASSES = []
folder_path = os.path.join(os.path.dirname(__file__), "files")

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        CLASSES.append(os.path.splitext(file)[0])

while(True):
    print(CLASSES)
    file_path = folder_path + "/" +input("Select a file: ") + ".txt"
    print(file_path)

    try:
        with open(file_path) as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: file doesn't exist")
    else:
        break

print(content)