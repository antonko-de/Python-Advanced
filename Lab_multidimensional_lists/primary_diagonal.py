'''Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). On the first line, 
you will receive an integer N – the size of a square matrix. 
The next N lines holds the values for each column - N numbers, separated by a single space. '''

rows = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

sum_prm_diag = 0

for index in range(rows):
    sum_prm_diag += matrix[index][index]
    
print(sum_prm_diag)
    
        