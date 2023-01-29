'''First, you will be given two sequences of integers values on different lines. 
The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
•	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
'''


nums_1 = set([int(x) for x in input().split()])
nums_2 = set([int(x) for x in input().split()])


RANGE = int(input())

for _ in range(RANGE):
    command = input().split()
    to_do, nums = ' '.join(command[0:2:]), [int(i) for i in command[2::]]

    if to_do == 'Add First':
        [nums_1.add(i) for i in nums]
    
    elif to_do == 'Add Second':
        [nums_2.add(i) for i in nums]
    
    elif to_do == 'Remove First':
        [nums_1.discard(i) for i in nums]
    
    elif to_do == 'Remove Second':
        [nums_2.discard(i) for i in nums]
    
    elif to_do == 'Check Subset':
        if nums_1.issubset(nums_2) or nums_2.issubset(nums_1):
            print(True)
        else:
            print(False)





print(*sorted(nums_1), sep=', ')
print(*sorted(nums_2), sep=', ')


   