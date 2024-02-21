"""
Switch case statement is a easy way to exectute logic based on different conditions
Python does not have a switch statement functionality.
Flexible alternative to the 'switch' statement in Python is stated here
"""

### Alternative Methods to run switch-case in python

# If-elif-else
city = 'Singapore'

if city == 'Tokyo':
    print('Tokyo')

elif city == 'Hong Kong':
    print('Hong Kong')

else:
    print('Singapore')

# Dictionary Mapping - Dictionary stores key-value pairs
country_dict = {
    1: "Singapore",
    2: "Tokyo",
    3: "Hong Kong"
}

def singapore():
    return "Singapore"
def tokyo():
    return "Tokyo"
def hongkong():
    return "Hong Kong"

def switch(selection):
    return country_dict.get(selection)()


# Python Classes
class CountrySwitch:
    def __init__(self):
        self.country_dict = {
            1: "Singapore",
            2: "Tokyo",
            3: "Hong Kong"
        }

    def singapore(self):
        return "Singapore"

    def tokyo(self):
        return "Tokyo"

    def hongkong(self):
        return "Hong Kong"

    def switch(self, selection):
        method_name = self.country_dict.get(selection)
        if method_name:
            method = getattr(self, method_name, self.default)
            return method()
        else:
            return self.default()

    def default(self):
        return "Unknown Country"
    
# Python Functions and Lambdas

# Keys are the selection numbers and the values are lambda functions returning the corresponding
country_dict = {
    1: lambda: "Singapore",
    2: lambda: "Tokyo",
    3: lambda: "Hong Kong"
}

def default():
    return "Unknown Country"

def switch(selection):
    return country_dict.get(selection, lambda: default)()

# Python 3.10 - Match Statement(Similar to switch statement)

def process_selection(selection):
    match selection:
        case 1:
            return "Singapore"
        case 2:
            return "Tokyo"
        case 3:
            return "Hong Kong"
        case _:
            return "Unknown Country"

# List of input values
selections = [1, 2, 3, 4]

# Map each selection to its corresponding case function
results = [process_selection(selection) for selection in selections]
