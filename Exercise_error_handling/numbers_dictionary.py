numbers_dictionary = {}

line = input()

while line != "Search":
    
    # handling non int value
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError as error:
        print('The variable number must be an integer!', error)
        
    line = input()

line =input()

while line != "Remove":
    
    # handling missing key value
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError as error:
        print("Number does not exist in dictionary!", error)
            
    line = input()

line = input()

while line != "End":
    
    # handling missing key value     
    try:
        searched = line
        del numbers_dictionary[searched] 
    except KeyError as error:
        print('Number does not exist in dictionary!', error)

    line = input()

print(numbers_dictionary)
