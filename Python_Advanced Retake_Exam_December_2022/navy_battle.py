
def cell_checker(cur_matrix:list, command:str, curr_place:tuple)->tuple:
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


hp = 3
btll_shps = 3
        
matrix_cells = int(input())

matrix = [list(input()) for _ in range(matrix_cells)]        

flag = False
for ind_row in range(matrix_cells):
    for ind_cols in range(matrix_cells):
        if matrix[ind_row][ind_cols] == 'S':
            curr_place = ind_row, ind_cols
            
           

matrix[curr_place[0]][curr_place[1]] = '-'


while (hp > 0)  and (btll_shps > 0) :
    command = input()
    next_field, curr_place = cell_checker(cur_matrix=matrix, command=command, curr_place=curr_place)
    
    if next_field == '*':
        hp -= 1
        
        matrix[curr_place[0]][curr_place[1]] = "-"
    
    elif next_field == 'C':
        btll_shps -= 1
        
        matrix[curr_place[0]][curr_place[1]] = "-"
        

if btll_shps > 0:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{curr_place[0]}, {curr_place[1]}]!")  

else:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
    
    
matrix[curr_place[0]][curr_place[1]] = "S"

for row in matrix:
    print(*row,sep="")