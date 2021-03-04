import os

try:
    path = "../file_writer/my_first_file.txt"
    os.remove(path)
    print("File deleted!")
except FileNotFoundError:
    print("File already deleted!")