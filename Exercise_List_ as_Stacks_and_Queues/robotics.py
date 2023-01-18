'''There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, 
product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). 
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output 
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
'''

from datetime import timedelta as timedelta 
from collections import deque as deque


def to_seconds(time:str) ->int:
    '''receive an hour and transform it into seconds
       
       params: time (str)- the time we want to convert into secs
    
       return: secs (int) - transformed into secs '''
    
    time_list = time.split(':')
    time_list.reverse()

    secs = 0
    for index, item in enumerate(time_list):
        secs += int(item) * ( 60 ** (index))
    
    return secs


def is_proccesing(rob):
    pass



robots = input()
robots_dict = {}

get_vals = lambda x: x.split('-')


        

for item in robots.split(';'):
    robot = get_vals(item)[0]
    proc_time = int(get_vals(item)[1])

    robots_dict[robot] = proc_time


starting_time = to_seconds(input())


products_q = deque()
robots_q = deque(robots_dict.keys())


while not product == 'End':



