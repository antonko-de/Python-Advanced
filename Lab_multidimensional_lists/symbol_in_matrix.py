'''Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines, you will receive rows of the matrix. 
Each row consists of ASCII characters. After that, you will receive a symbol. 
Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". 
You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".'''



cells = int(input())

matrix = [list(input()) for _ in range(cells)]

to_find = input()

result=[]
for ind_row in range(cells):
    for ind_col in range(cells):
        if matrix[ind_row][ind_col] == to_find:
            result.append((ind_row, ind_col))
            

if result:
    print(result[0])
    
else:
    print(to_find + ' does not occur in the matrix')