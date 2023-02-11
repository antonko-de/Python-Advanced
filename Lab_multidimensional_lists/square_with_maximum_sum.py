'''Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values. 
On first line you will get matrix sizes in format "{rows}, {columns}".  
On the next rows, you will get elements for each column, separated with a comma and a space ", ". 
You should print the found submatrix and the sum of its elements, as shown in the examples. 
'''

rows , cols = list(map(int, input().split(', ')))

matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

max_sub = 0
max_mat = []

for row in range(rows - 1):
    for col in range(0, cols - 1, 1):
        sub_1 = matrix[row][col]
        sub_2 = matrix[row][col+1]
        sub_3 = matrix[row+1][col]
        sub_4 = matrix[row+1][col+1]
        max_it = sub_1 + sub_2 + sub_3 + sub_4
        if max_sub < max_it:
            max_sub = max_it
            max_mat = [[sub_1, sub_2], [sub_3, sub_4]]
            
            

for row in max_mat: print(*row)

print(max_sub)