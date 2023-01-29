'''You are learning how to make milkshakes.
First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. 
If their values are equal, you should make a milkshake and remove both ingredients. 
Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
Input
•	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
•	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
•	On the first line, print:
o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
o	Otherwise: "Not enough milkshakes."
•	On the second line - print:
o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
o	Otherwise: "Chocolate: empty"
•	On the third line - print:
o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
o	Otherwise: "Milk: empty"
Constraints
•	All given numbers will be valid integers in the range [-100 … 100].
'''
from collections import deque

SHAKE_GOAL = 5
NO_MILKSHAKES = 'Not enough milkshakes.'
CH_EMPTY = 'Chocolate: empty'
MLK_EMPTY = 'Milk: empty'

chocos = deque(input().split(', '))
milk = deque(input().split(', '))

shakes = 0

while not shakes == SHAKE_GOAL and chocos and milk:
    
   curr_choco = int(chocos.pop())
   curr_milk = int(milk.popleft())


   if curr_choco <= 0 and curr_milk <=0:
        continue 
    
   if curr_choco <= 0:
        milk.appendleft(curr_milk)
        continue
    
   elif curr_milk <= 0:
        chocos.append(curr_choco)
        continue

   if curr_choco == curr_milk:
        shakes += 1
    
   else:
        milk.append(curr_milk)
        chocos.append(curr_choco - 5)


if shakes == SHAKE_GOAL:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(i) for i in chocos) or 'empty'}")
print(f"Milk: {', '.join(str(i) for i in milk) or 'empty'}")