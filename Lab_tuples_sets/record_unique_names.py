'''Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
'''

RANGE = int(input())

names = set([input() for x in range(RANGE)])

for i in names: print(i)