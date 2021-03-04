def get_info(**kwargs):
    person = {"name": kwargs.get("name"), "town": kwargs.get("town"), "age": kwargs.get("age")}
    return f"This is {person['name']} from {person['town']} and he is {person['age']} years old"


# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))