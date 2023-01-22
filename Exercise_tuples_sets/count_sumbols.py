'''Write a program that reads a text from the console and counts the occurrences of each character in it. 
Print the results in alphabetical (lexicographical) order.'''


message = tuple(input())

ocur_dict = {i : message.count(i) for i in message }

sorted_dict = dict(sorted(ocur_dict.items(), key=lambda item: item[0]))

for a,b in sorted_dict.items(): 
    print(f"{a}: {b} time/s")