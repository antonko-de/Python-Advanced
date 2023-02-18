'''Your friend Stamat is working on a new AI program. Like every irresponsible teenager, he programs all night and, of course, drinks a lot of energy drinks.
Stamat's friends are concerned about him and want you to create a program that tells him when to stop the energy drinks and start drinking water.
On the first line, you will receive a sequence of numbers representing milligrams of caffeinе. On the second line, you will receive another sequence of numbers 
representing energy drinks. 
It is important to know that the maximum caffeine Stamat can have for the night is 300 milligrams, and his initial is always 0.
To calculate the caffeine in the drink take the last milligrams of caffeinе and the first energy drink, and multiply them. Then, compare the result with the caffeine 
Stamat drank:
•	If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams, remove both the milligrams of caffeinе 
and the drink from their sequences. Also, add the caffeine to Stamat's total caffeine.
•	If Stamat is about to exceed his maximum caffeine per night, do not add the caffeine to Stamat’s total caffeine. Remove the milligrams of caffeinе 
and move the drink to the end of the sequence. Also, reduce the current caffeine that Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).
Stop calculating when you are out of drinks or milligrams of caffeine.
For more clarification, see the examples below.
Input
•	In the first line, you will be given a sequence of the milligrams of caffeinе - integers separated by comma and space ", " in the range [1, 50]
•	In the second line, you will be given a sequence of energy drinks - integers separated by comma and space ", " in the range [1, 300]
Output
•	On the first line:
o	If Stamat hasn't drunk all the energy drinks, print the remaining ones separated by a comma and a space ", ": 
	"Drinks left: { remaining drinks separated by ", " }"
o	If Stamat has drunk all the energy drinks, print:
	"At least Stamat wasn't exceeding the maximum caffeine."
•	On the next line, print:
o	"Stamat is going to sleep with { current caffeine } mg caffeine."
Constraints
•	You will always have at least one element in each sequence at the beginning
'''

#input coffeine comma separated pop
#input energy drings comma separated poleft
#var for total coff
#get the num of the drinks with the min len of the two elements
# build the logic:
    # calculate coff amount
    # compare
    # if less than 300 remove both and add to total coff
    # if more than 300 remove caffeine and append dring remove 30 from the total coff
    # everything is while you have drinks and caff
#build the print logic:
    # if there are drinks print them
    # if no do the other print
    # print out total caff

from collections import deque

coffs = deque(list(map(int, input().split(', '))))
drinks = deque(list(map(int, input().split(', '))))

total_coff = 0

while drinks and coffs:
    curr_coff = coffs.pop()
    curr_drink = drinks.popleft()
    
    curr_amount = curr_coff * curr_drink
    
    if (curr_amount + total_coff)  > 300:
        total_coff -= 30
        drinks.append(curr_drink)
        if total_coff < 0:
            total_coff = 0
    else:
        total_coff += curr_amount
    
if drinks:
    print('Drinks left: ',end='')
    print(*drinks,sep=", ")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
    
print(f"Stamat is going to sleep with {total_coff} mg caffeine.")  