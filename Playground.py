y = '+'
a = [str(x) + str(y) for x in [1,3,4]]
b = ''.join(a)[:-1:]

print(eval(b))