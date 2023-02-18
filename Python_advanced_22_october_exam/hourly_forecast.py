'''3. Hourly Forecast
Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can see the most sights. 
Patricia is busy at work and doesn't have time to think about the perfect place for her vacation, so she wants your help.
Write a function called forecast that stores information about the weather, and returns sorted information for all locations. 
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the location, 
and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. 
First are positioned the locations with sunny weather, 
next are the locations with cloudy weather, and last are the locations with rainy weather. 
For each sequence of locations (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"
Constraints
•	Each tuple given will always contain the location with its weather.
•	You will never receive the same location twice or more times.
Examples
'''

def forecast(*args):
    
    sunny = [x[0] for x in args if x[1]== 'Sunny']
    sunny.sort() 
    cloudy = [x[0] for x in args if x[1]== 'Cloudy']
    cloudy.sort()
    rainy = [x[0] for x in args if x[1]== 'Rainy']
    rainy.sort()
    
    result = ''
    for item in sunny:
        result += f"{item} - Sunny\n"
    for item in cloudy:
        result += f"{item} - Cloudy\n"
    for item in rainy:
        result += f'{item} - Rainy\n'
    return result[:-1:]

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


    