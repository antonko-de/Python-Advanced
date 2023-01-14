'''There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
For each petrol pump, you will receive two pieces of information (separated by a single space): 
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol per 1 kilometer,
 and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. 
You never miss filling its tank at a petrol pump.
Input
•	On the first line, you will receive the number of petrol pumps - N
•	On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between 
that petrol pump and the next petrol pump, separated by a single space
Output
•	An integer which will be the smallest index of a petrol pump from which you can start the tour
Constraints
•	1 ≤ N ≤ 1000001
•	1 ≤ amount of petrol, distance ≤ 1000000000
•	You will always have at least one point from where the truck will be able to complete the circle
'''
from collections import deque

def get_vals(info:str)->tuple: 

    '''get the petrol vol filled and the distance to the next pump

       params:info(string) - the unparsed information
       
       returns: values (tuple) - the parsed information
    '''
    vol = int(info[0])
    dist = int(info[1])

    return vol, dist




def full_travel_check(crc_q:deque, pump_num:int) -> bool:
    '''checks if the full lap circle can be completed
       
       params: crc_q (deque) - current lap circle setup
               pump_num (int) - number of stops
       returns: boolean
    '''
    counter = 0
    vol_total = 0
    for point in crc_q:

        vol, dist = get_vals(point)
        vol_total += vol
        diff = vol_total - dist
        if diff >= 0 :
            counter += 1
            vol_total = diff
        else:
            break

    if counter == pump_num:
        return True
    else:
        return False



pmp_num = int(input())
    
list_stops = [get_vals(tuple(input().split())) for x in range(pmp_num)]

crc_q = deque(list_stops)

check = full_travel_check(crc_q, pmp_num)

while check == False:
    crc_q.append(crc_q.popleft())
    check = full_travel_check(crc_q, pmp_num)

start_point = crc_q.popleft()

print(list_stops.index(start_point))


    
    
    


        
