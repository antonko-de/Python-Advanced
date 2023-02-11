'''Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. 
There will be no case with two or more 3x3 squares with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
•	On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
Output
•	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
•	On the following 3 lines, print each element of the found submatrix, separated by a single space
'''

rows, columns = list(map(int,input().split()))

matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = -123333333333333333333333333333333333123213123123213123
max_sub_mat = []
for row_i in range(1, rows-1):
    for col_i in range(1, columns-1):
        sub_1 = matrix[row_i-1][col_i-1]
        sub_2 = matrix[row_i-1][col_i]
        sub_3 = matrix[row_i-1][col_i+1]
        sub_4 = matrix[row_i][col_i-1]
        sub_5 = matrix[row_i][col_i]
        sub_6 = matrix[row_i][col_i+1]
        sub_7 = matrix[row_i+1][col_i-1]
        sub_8 = matrix[row_i+1][col_i]
        sub_9 = matrix[row_i+1][col_i+1]
        all_subs = [sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7,sub_8,sub_9]
        sum_sub = sum(all_subs)
        if sum_sub > max_sum:
            max_sum = sum_sub
            max_sub_mat = [all_subs[:3:],
                          all_subs[3:6:],
                          all_subs[6::]]
        
        
        
print(f"Sum = {max_sum}")
for row in max_sub_mat:
    print(*row)