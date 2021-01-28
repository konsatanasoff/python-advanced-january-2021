

data = input()
user_data = {}

while not data.isdigit():
    name, number = data.split('-')

    user_data[name] = number
    data = input()

for i in range(int(data)):
    contact = input()
    if contact in user_data:
        print(f"{contact} -> {user_data[contact]}")
    else:
        print(f"Contact {contact} does not exist.")