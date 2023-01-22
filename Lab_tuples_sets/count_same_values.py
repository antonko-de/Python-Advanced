'''You will be given numbers separated by a space. Write a program that prints 
the number of occurrences of each 
number in the format "{number} - {count} times". 
The number must be formatted to the first decimal point.'''

nums = tuple("{0:.1f}".format(float(i)) for i in input().split())

cnt_dict = { x : nums.count(x) for x in nums}

for num, count in cnt_dict.items():
    print(f"{num} - {count} times")