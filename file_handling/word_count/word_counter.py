import re


def get_content(file_path):
    with open(file_path, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


def write_result(result):
    with open("output", "w") as file:
        file.writelines("\n".join(result))


words_path = "words.txt"
text_path = "text.txt"

word_file_content = get_content(words_path)
text_file_content = get_content(text_path)

word_data = {}

for word in text_file_content:
    if word in word_file_content:
        word_data[word] = text_file_content.count(word)

sorted_data = [f"{el[0]} - {el[1]}" for el in sorted(word_data.items(), key=lambda x: -x[1])]

write_result(sorted_data)
