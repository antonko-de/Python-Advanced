'''You are given an algebraic expression with parentheses. 
Scan through the string and extract each set of parentheses
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'''

EXPRESSION = list(input())

stack = []

enum_expression = enumerate(EXPRESSION)

for index, item in enum_expression:
    if item == '(':
        stack.append(index)
    
    if item == ')':
        opening_index = stack.pop()
        closing_index = index
        print(''.join(EXPRESSION[opening_index:closing_index+1:]))
