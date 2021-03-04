string = input()

stack = []

for i in range(len(string)):
    char = string[i]
    if char == '(':
        stack.append(i)
    elif char == ')':
        j = stack.pop()
        print(string[j:i + 1])
