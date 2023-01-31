'''You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
•	NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
•	MustContainAtSymbolError - raise it when there is no "@" in the email
•	InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
•	NameTooShortError - "Name must be more than 4 characters"
•	MustContainAtSymbolError - "Email must contain @"
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one
'''

class NameTooShortError(Exception):
    message = "Name must be more than 4 characters"

class MustContainAtSymbolError(Exception):
    message = "Email must contain @"

class InvalidDomainError(Exception):
    message = "Domain must be one of the following: .com, .bg, .org, .net"


VALID_DOMAINS = [".com", ".bg", ".org", ".net"]


def validate_email(email:str)->str: 
    '''validates the correct format of the given email
       or raises appropriate error
       
       params: email (string) - email to validate
       
       returns: valid email (str) or raises error'''
    
    parsed_email = email.split('@')

    if len(parsed_email) < 2:
        raise MustContainAtSymbolError(MustContainAtSymbolError.message)
    else:
        name, domain = parsed_email

    if len(name) < 5:
        raise NameTooShortError(NameTooShortError.message)
           
    if not any(map(lambda x: domain.endswith(x), VALID_DOMAINS)):
        raise InvalidDomainError(InvalidDomainError.message)
    
    print('Email is valid')
    
    

email = input()

while not email == 'End':
    
    validate_email(email=email)
   
    email = input()

