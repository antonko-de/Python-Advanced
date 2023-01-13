'''3. Supermarket

Tom is working at the supermarket, and he needs your help to keep track of his clients. 
Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until "
End" is received. If, in the meantime, you receive the command "Paid", 
you should print each customer in the order they are served (from the first to the last one) and empty the queue.

When you receive "End", you should print the count of the remaining people in the queue in the format: 
"{count} people remaining.".'''

from collections import deque as Deque

market_deque = Deque()


INPUT_PAID = 'Paid'
INPUT_END = 'End'


while True:
    name = input()

    if name == INPUT_END:
        print(f"{len(market_deque)} people remaining.")
        break


    elif name == INPUT_PAID:
        while len(market_deque) > 0:
            print(market_deque.popleft())
        

    else:
        market_deque.append(name)


#holder