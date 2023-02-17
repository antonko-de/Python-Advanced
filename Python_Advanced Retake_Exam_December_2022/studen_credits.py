'''Write a function students_credits which receives a different number of strings. 
Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets are proportional to his points on the test.
For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test points, he will get 12.5 credits for the course.
Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's credits.
Finally, return a string on multiple lines containing:
•	Diyan's achievement message:
o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
•	Information for each course and Diyan's credits:
o	"{course name} - {diyan's credits}"
o	Note: Each course data should be on a new line.
•	All credits must be formatted to the first decimal place.

Note: Submit only the function in the judge system
Input
•	There will be no input, just any number of strings with courses data passed to your function
Output
•	The function should return a string in the format described above:
Constraints:
•	There will always be at least one course.
•	There will not be two or more courses with the same name.
•	All points and all credits will be whole numbers
'''

def students_credits(*args:str)->str:
    DIPLOMA = 240
    
    parsed_records = [record.split('-') for record in list(args)]
    
    courses_grained = {}
    
    for record in parsed_records:
        course, creds, max_points, d_points = record
        
        actual_creds = int(d_points) / int(max_points) * int(creds)

        courses_grained[course] = actual_creds
    
    total_creds = sum(courses_grained.values())
    sorted_courses_grained = dict(sorted(courses_grained.items(), key=lambda x:x[1],reverse=True))
    
    if total_creds >= DIPLOMA:
        result = f"Diyan gets a diploma with {round(total_creds,1)} credits.\n"
        for course, creds_sorted in sorted_courses_grained.items():
            result+= f"{course} - {round(creds_sorted,1)}\n"
    
    else:
        result = f"Diyan needs {round(DIPLOMA-total_creds,1)} credits more for a diploma.\n"
        for course, creds_sorted in sorted_courses_grained.items():
            result+= f"{course} - {round(creds_sorted,1)}\n"     
    
    
    return result[:-1:]

    
        
        
        
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)



