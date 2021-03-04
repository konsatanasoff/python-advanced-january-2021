import os


def extract_files(my_dir):
    return [el for el in my_dir if os.path.isfile(el)]


def get_extensions(files):
    report = {}

    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


# path = "../../file_handling"
dir_content = os.listdir()

files = extract_files(dir_content)

report_info = get_extensions(files)

result = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result += f".{extension}\n"
    for name in file_names:
        result += f"- - - {name}.{extension}\n"

with open("C:\\Users\\User\\Desktop\\report_result.txt", "w") as file:
    file.write(result)