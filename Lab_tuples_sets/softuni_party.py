'''There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. 
When a guest comes, check if they exist on any of the two reservation lists.
On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their reservation codes. 
All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of guests who did not come to the party and their reservation numbers:
•	The VIP guests must be first.
•	Both the VIP and the Regular guests must be sorted in ascending order.
'''

RESERVATION_NUMBER = int(input())

reservations = set([input() for _ in range(RESERVATION_NUMBER)])

come_ins = []
command = input()

while not command == 'END':
    come_ins.append(command)
    command = input()

skipped = reservations.difference(set(come_ins))

vips = [i for i in skipped if i[0].isdigit()]
norm = [i for i in skipped if not i[0].isdigit()]
vips.sort()
norm.sort()
vips.extend(norm)

print(len(vips))

for i in vips: print(i)