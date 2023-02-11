els = int(input())

matrix = [list(map(int, input().split())) for _ in range(els)]

sum_prim = 0
sum_sec = 0



for ind_row in range(els):
        prim_num = matrix[ind_row][ind_row]
        sum_prim += prim_num

        
        sec_num =  matrix[ind_row][-1 - ind_row]
        sum_sec += sec_num
    
print(abs(sum_prim - sum_sec))   
     
