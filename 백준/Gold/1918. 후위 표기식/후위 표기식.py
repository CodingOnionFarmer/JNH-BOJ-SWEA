formula = input()
postfix_formula = ''
stack = []
for char in formula:
    if char.isalpha():
        postfix_formula += char
    else:
        if char == '(':
            stack.append(char)
        elif char == ')':
            while True:
                operator = stack.pop()
                if operator == '(':
                    break
                postfix_formula += operator
        elif char == '+' or char == '-':
            while stack:
                operator = stack.pop()
                if operator == '(':
                    stack.append(operator)
                    break
                postfix_formula += operator
            stack.append(char)
        else:
            while stack:
                operator = stack.pop()
                if operator in {'+', '-', '('}:
                    stack.append(operator)
                    break
                postfix_formula += operator
            stack.append(char)
while stack:
    char = stack.pop()
    postfix_formula += char
print(postfix_formula)
