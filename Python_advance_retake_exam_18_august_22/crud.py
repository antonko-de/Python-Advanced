'''In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information. 
It consists of:
•	Letters - on one or many positions in the table
•	Numbers - on one or many positions in the table
•	Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
•	"Create, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"
o	If the position is NOT empty, do NOT create a value on that position
•	"Update, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"
o	If the position is empty, do NOT update the value on that position
•	"Delete, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
o	If the position is already empty, do NOT delete it
•	"Read, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, print it on the console
o	If the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.
Input
•	On the first 6 lines - a matrix with positions separated by a single space
o	Letters are in the range [a-zA-Z]
o	Numbers are in the range [-100, 100]
•	On the next line - your first position in the format: "({row}, {column})"
•	On the following lines until you receive the command "Stop" - commands in the format shown above
Output
•	In the end, print the final matrix, each row on a new line, each position separated by a single space.
Constraints
•	You will always receive valid coordinates
•	You will always receive directions in the range of the table
•	You will always receive letters or numbers
'''

def cell_checker(cur_matrix:list, command:str, curr_place:list)->tuple:
    curr_row = curr_place[0]
    curr_col = curr_place[1]
    if command == "up":
        to_check = cur_matrix[curr_row -1 ][curr_col]
        curr_place = curr_row -1, curr_col
    elif command == 'down':
        to_check = cur_matrix[curr_row + 1 ][curr_col]
        curr_place = curr_row + 1, curr_col
    elif command == 'left':
        to_check = cur_matrix[curr_row][curr_col-1]
        curr_place = curr_row, curr_col-1
    elif command == 'right':
        to_check = cur_matrix[curr_row][curr_col+1] 
        curr_place = curr_row, curr_col+1
    
    return to_check, curr_place

EMPTY = '.'
CELLS = 6

matrix = [input().split() for _ in range(CELLS)]
curr_place = [int(i) for i in input() if i.isnumeric()]


command = input()

while not command == 'Stop':
    to_do, direction, *val = command.split(', ')
    to_check, curr_place =cell_checker(cur_matrix=matrix,command=direction,curr_place=curr_place)
    
    if to_do == 'Create':
        if to_check is EMPTY:
            matrix[curr_place[0]][curr_place[1]] = val[0]
            
    elif to_do == 'Update':
        if not to_check is EMPTY:
            matrix[curr_place[0]][curr_place[1]] = val[0]
            
    elif to_do == 'Delete':
        if not to_check is EMPTY:
            matrix[curr_place[0]][curr_place[1]] = EMPTY
            
    elif to_do == 'Read':
        if not to_check is EMPTY:
            print(matrix[curr_place[0]][curr_place[1]])
    
    command = input()
            

for row in matrix:
    print(*row, sep=' ')            
