vowels = ['a', 'e', 'u', 'o', 'i']
text = [el for el in input() if el not in vowels]
print(''.join(text))