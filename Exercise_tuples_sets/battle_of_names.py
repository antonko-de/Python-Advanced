'''You will receive a number N. On the following N lines, you will be receiving names. 
You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). 
Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
•	If the sums of the two sets are equal, print the union of the values, separated by ", ". 
•	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set
'''

RANGE = int(input())

odd_set = set()
even_set = set()

for row in range(RANGE):
    sum_chars = sum([ord(x) for x in list(input())])
    sum_chars //= row + 1
    
    if sum_chars % 2 == 0:
        even_set.add(sum_chars)
    else:
        odd_set.add(sum_chars)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_even == sum_odd:
    print(', '.join([str(x) for x in odd_set.union(even_set)]))

elif sum_odd > sum_even:
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))

else:
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))