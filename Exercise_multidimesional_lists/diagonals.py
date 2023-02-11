'''Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". 
You should find the matrix's diagonals, prints them and their sum in the format:

"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}

Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}"'''

els = int(input())

matrix = [list(map(int, input().split(','))) for _ in range(els)]

sum_prim = 0
sum_sec = 0

prim_diag = ''
sec_diag = ''

for ind_row in range(els):
        prim_num = matrix[ind_row][ind_row]
        sum_prim += prim_num
        prim_diag += ", " + str(prim_num)
        
        sec_num =  matrix[ind_row][-1 - ind_row]
        sum_sec += sec_num
        sec_diag += ", " + str(sec_num)
   
     
print(f"Primary diagonal:{prim_diag[1::]}. Sum: {sum_prim}")
print(f"Secondary diagonal:{sec_diag[1::]}. Sum: {sum_sec}")
