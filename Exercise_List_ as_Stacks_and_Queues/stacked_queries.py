'''You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. 
Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
'''
queries_num = int(input())

stack = []

for num in range(queries_num):

    query = input()

    if '1' in query:
        val = query.split()[1]
        stack.append(val)

    elif query == '2':
        if stack:
            stack.pop()

    
    elif query == '3':
        if stack:
            print(max(stack))

    else:
        if stack:
            print(min(stack))

print(', '.join(stack[::-1]))