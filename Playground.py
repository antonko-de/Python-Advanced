
def success_pairs_check(current_crafted_presents:list)->bool:
    check_1 = ('Doll', 'Train')
    check_2 = ('Teddy Bear', 'Bicycle') 
    
    if check_1[0] in current_crafted_presents and check_1[1] in current_crafted_presents:
        return True
    elif check_2[0] in current_crafted_presents and check_2[1] in current_crafted_presents:
        return True
    else:
        return False

b = ['Doll', 'a', 'c']
c = ['Doll', 'Train']


print(success_pairs_check(c))