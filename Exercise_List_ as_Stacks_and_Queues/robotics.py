'''There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a 
product for processing and log its name, 
product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at 
[start time + 1 second]). 
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;
robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output 
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
'''

from datetime import datetime, timedelta 
from collections import deque 


class mrRobot():
    '''a mrRobot class which will replicate very basic
         robot unit memory infra'''
    
    def __init__(self,  unit_name:str, proc_cap:int, time_left_proc = 0):
        self.unit_name = 'unitName' + unit_name
        self.proc_cap = int(proc_cap)
        self.time_left_proc = time_left_proc
        


# def to_seconds(time:str) ->int:
#     '''receive an hour and transform it into seconds
       
#        params: time (str)- the time we want to convert into secs
    
#        return: secs (int) - transformed into secs '''
    
#     time_list = time.split(':')
#     time_list.reverse()

#     secs = 0
#     for index, item in enumerate(time_list):
#         secs += int(item) * ( 60 ** (index))
    
#     return secs


# def to_prop_time_format(secs:int) -> str:
#     '''reformats the time as we need it
       
#        params: secs (int)

#        return: frmt_time (string) - the time as we need it ot look
#     '''

#     hours, remainder = divmod(secs, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return ('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))

      


robot_caps = input().split(";")

get_vals = lambda x: x.split('-')

robots_parsed = [get_vals(x) for x in robot_caps]
robots_pack = { x[0] : mrRobot(x[0], x[1]) for x in robots_parsed}

curr_time = datetime.strptime(input(), "%H:%M:%S")
product = input()
all_products = deque()

while not product == 'End': 
    all_products.append(product)
    product = input()

while all_products:
    curr_time += timedelta(0, 1)
    curr_product = all_products.popleft()
    
    
    for name, unit in robots_pack.items():
        
        if unit.time_left_proc > 0:
            robots_pack[name].time_left_proc -= 1
    
    free_units = list(filter(lambda x: x[1].time_left_proc == 0, robots_pack.items()))
    

    
    if not free_units:
        all_products.append(curr_product)
        continue
    
    curr_robot = free_units[0][0]
    robots_pack[curr_robot].time_left_proc = robots_pack[curr_robot].proc_cap
    print(f'{free_units[0][0]} - {curr_product} [{curr_time.strftime("%H:%M:%S")}]')

 





    





            





