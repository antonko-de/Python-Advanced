'''Write a program that finds the longest intersection. You will be given a number N. 
On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". 
You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: 
"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
'''

RANGE = int(input())

ranges = [[i.split(',') for i in input().split('-')] for _ in range(RANGE)]

longest_len = 0
longest_set = {}
for duo in ranges:
    r_1_1, r_1_2 = int(duo[0][0]), int(duo[0][1])
    r_2_1, r_2_2 = int(duo[1][0]), int(duo[1][1])
    set_1 = {x for x in range(r_1_1, r_1_2 + 1)}
    set_2 = {x for x in range(r_2_1, r_2_2 + 1)}

    curr_inters = set_1.intersection(set_2)

    if len(curr_inters) > longest_len:
        longest_len = len(curr_inters)
        longest_set = curr_inters

longest_intersec = [str(x) for x in longest_set]
print(f"Longest intersection is [{', '.join(longest_intersec)}] with length {longest_len}")