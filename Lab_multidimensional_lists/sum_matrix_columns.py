'''Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space. 
'''


rows, cols = list(map(int, input().split(', ')))

matrix = [list(map(int, input().split())) for _ in range(rows)]

all_sums = []

for col in range(cols):
    sum_curr_col = 0
    for row in range(rows):
        sum_curr_col += matrix[row][col]
        
    all_sums.append(sum_curr_col)
    

print(*all_sums, sep='\n')