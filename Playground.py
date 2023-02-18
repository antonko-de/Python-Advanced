def find_exit(matrix:list)->tuple:
    for row in matrix:
        if 'T' in row:
            curr_place = matrix.index(row), row.index('T')
            
        return curr_place
    
    
    
    matrix = [['.', '.', '.', '.', '.']
    ['.', '.', '.', '.', '.']
    ['.', '.', '.', '.', '.']
    ['.', 'T', '.', '.', '.']
    ['.', '.', 'F', '.', '.']]
    
    
    print(find_exit(matrix=matrix))