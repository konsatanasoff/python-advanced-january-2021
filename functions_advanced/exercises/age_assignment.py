def age_assignment(*args,**kwargs):
    names = args
    data = kwargs
    result = {}

    for name in names:
        for k, v in data.items():
            if k in name:
                result[name] = v
    return result


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
