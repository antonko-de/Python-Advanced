'''Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, 
you will receive the matrix's dimensions in the format "{rows} {columns}". 
On the following rows, you will receive characters separated by a single space.
Print the number of all square matrices you have found.'''

rows, cols = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]

counter = 0
for row in range(rows - 1):
    for col in range(0, cols - 1, 1):
        sub_1 = matrix[row][col]
        sub_2 = matrix[row][col+1]
        sub_3 = matrix[row+1][col]
        sub_4 = matrix[row+1][col+1]
        
        if len({sub_1,sub_2,sub_3,sub_4}) == 1:
            counter += 1
            
print(counter)