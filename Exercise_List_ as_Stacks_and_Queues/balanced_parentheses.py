'''You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. 
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs 
after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: 
(), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output 
•	For each test case, print on a new line "YES" if the parentheses are balanced. 
•	Otherwise, print "NO"
Constraints
•	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
•	Each character of the sequence will be one of {, }, (, ), [, ]
'''
from collections import deque



prnth_deque = deque(input())
open_prnth = deque()



while prnth_deque:
    
    curr_prnth = prnth_deque.popleft()

    if curr_prnth in "[({":
        open_prnth.append(curr_prnth)
    
    elif not open_prnth:
        print('NO')
        break

    else:
        if f"{open_prnth.pop() + curr_prnth}" not in "{}()[]":
            print('NO')
            break

else:
    print('YES') 
