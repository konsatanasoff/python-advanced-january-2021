import os


def create(file_path):
    with open(file_path, "w") as file:
        file.write('')


def add(file_path, content):
    with open(file_path, "a") as file:
        file.write(content+"\n")


def replace(file_path, old_str, new_str):
    try:
        with open(file_path, "r+") as file:
            text = ' '.join(file.readlines())
            replaced = text.replace(old_str, new_str)
            file.seek(0)
            file.write(replaced)
    except FileNotFoundError:
        print("An error occurred")


def delete(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


def start_operation():
    data = input().split("-")
    while not data[0] == "End":
        command, command_args = data[0], data[1:]
        mapper[command](*command_args)
        data = input().split("-")


mapper = {"Create": create,
          "Add": add,
          "Replace": replace,
          "Delete": delete}


start_operation()
