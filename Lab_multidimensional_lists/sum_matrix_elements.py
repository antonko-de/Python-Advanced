'''
Write a program that reads a matrix from the console and prints:
•	The sum of all numbers in the matrix
•	The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ". 
'''

rows, columns = map(int, input().split(','))

matrix = []

for row in range(rows):
    matrix.append((list(map(int, input().split(',')))))
 
sum_all = sum([sum(i)for i in matrix])


print(sum_all)
print(matrix)