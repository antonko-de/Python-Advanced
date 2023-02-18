'''You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}". 
You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. 
Next, take the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats. 
If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches 
•	You have made a total of 10 rotations
Input
•	On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
•	On the second and the third line, you will be given two more sequences - integers separated by a comma and a space ", "
Output
When the program ends, print the following on two different lines:
o	Seat matches: {matches separated by comma and space}
o	Rotations count: {total rotations made}
Constraints
•	All integers will be in the range [1, 100]
•	All letters will be in the range [A-Z]
•	You will never run out of numbers in your sequences before the program ends
•	You will never have more than one match at a time
'''

from collections import deque

seats =  input().split(', ')

frst_sq = deque(map(int, input().split(', '))) #popleft
scnd_sq = deque(map(int, input().split(', '))) #pop

MAX_ROTATIONS = 10
mtchng_sts = 0
rtns =0

taken_seats = []
while mtchng_sts < 3 and rtns < MAX_ROTATIONS:
    curr_frst = frst_sq.popleft()
    curr_scnd = scnd_sq.pop()
    
    char = chr(curr_frst+curr_scnd)
    
    to_check = []
    
    for seat in seats:
        if char in seat:
            to_check.append(seat)
    flag = False       
    for num in [curr_frst,curr_scnd]:
        for seat in to_check:
            if num == int(seat[:-1:]):
                taken_seats.append(seat)
                mtchng_sts += 1
                flag = True
    
    for taken in taken_seats:
        try:
            seats.remove(taken)
        except ValueError as e:
            pass
    
    if not flag:
        frst_sq.append(curr_frst)
        scnd_sq.appendleft(curr_scnd)
    flag = False
        
    rtns += 1
    

print("Seat matches: ",end='')
print(*taken_seats,sep=', ')
print(f"Rotations count: {rtns}")
    
