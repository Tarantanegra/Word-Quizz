import json
import random
import os

CLASSES = []
folder_path = os.path.join(os.path.dirname(__file__), "files")

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        CLASSES.append(os.path.splitext(file)[0])

print(CLASSES)