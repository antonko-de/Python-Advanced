'''Write program that:

· Reads an input string

· Reverses it using a stack

· Prints the result back on the console'''


stack = list(input())

while len(stack) > 0:
    print(stack.pop(), end='')

        