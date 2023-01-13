
'''Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, 
you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". 
Add those people in a queue. Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
'''
from collections import deque as Deque

water_deque = Deque()

water_volume = int(input())

START_COMMAND = 'Start'
REFILL_COMMAND = 'refill'
END_COMMAND = 'End'

while True:
    command = input()

    if command == END_COMMAND:
                print(f"{water_volume} liters left")
                break

    if command == START_COMMAND:
        
        while len(water_deque) > 0:
            vol_command = input()

            if command == END_COMMAND:
                print(f"{water_volume} liters left")
                break
            
            elif REFILL_COMMAND in vol_command:
                water_volume += int(vol_command.split()[1])
            
            else:
                needed_water = int(vol_command)
                cur_name = water_deque.popleft()
            
                if needed_water <= water_volume:
                    water_volume -= needed_water
                    print(f'{cur_name} got water')

                else:
                    print(f'{cur_name} must wait')

    else:
        water_deque.append(command)            

        
    


