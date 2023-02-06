'''This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:


Present	Magic needed
Doll	150
Wooden train	250
Teddy bear	300
Bicycle 	400

You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level.+
 If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
•	If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
•	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
•	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
•	a doll and a train
•	a teddy bear and a bicycle
Input
•	The first line of input will represent the values of boxes with materials - integers, separated by a single space
•	On the second line, you will be given the magic values - integers again, separated by a single space
Output
•	On the first line - print whether you've succeeded in crafting the presents:
o	"The presents are crafted! Merry Christmas!"
o	"No presents this Christmas!"
•	On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
•	On the next lines print the presents you have crafted, ordered alphabetically in the format:
o	"{toy_name1}: {amount}
{toy_name2}: {amount}
{toy_nameN}: {amount}"
'''
# import dependencies
from collections import deque

# func that checks for completion
def success_pairs_check(current_crafted_presents:list)->bool:
    check_1 = ('Doll', 'Wooden train')
    check_2 = ('Teddy bear', 'Bicycle') 
    
    if check_1[0] in current_crafted_presents and check_1[1] in current_crafted_presents:
        return True
    elif check_2[0] in current_crafted_presents and check_2[1] in current_crafted_presents:
        return True
    else:
        return False


# create presents reqs dict
PRNT_REQS = {150 : 'Doll',
             250 : 'Wooden train',
             300: 'Teddy bear',
             400 : 'Bicycle' }

#input materials and magic level
mats = deque([int(i) for i in input().split()])
magic = deque([int(i) for i in input().split()])
crafted_toys = []

#while loop checking materials, magic and if the compl check tuples is in the the ready list
while mats and magic:
    curr_mat = mats.pop()
    curr_magic = magic.popleft()
    combi = curr_mat * curr_magic
    
    if curr_magic == 0 or curr_mat == 0:
        if curr_magic != 0:
            magic.appendleft(curr_magic)
        elif curr_mat != 0:
            mats.append(curr_mat)
        continue
    
    if combi < 0:
        mats.append(curr_mat+curr_magic)
        
    elif not combi in PRNT_REQS.keys() and combi >= 0:
        mats.append(curr_mat + 15)
        
    elif combi in PRNT_REQS.keys():
        crafted_toys.append(PRNT_REQS.get(combi))

 
if success_pairs_check(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
  
#print materials magic left or skip  
if mats:
    mats.reverse()
    print(f"Materials left: {', '.join(str(x) for x in mats)}")
    
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

#print presents crafter alphabetically
crafted_toys.sort()

toy_counts = [(i, crafted_toys.count(i)) for i in crafted_toys]

for item in sorted(list(set(toy_counts))):
    print(f"{item[0]}: {item[1]}")    