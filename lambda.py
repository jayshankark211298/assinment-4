"""
Define a list named 'data' containing some numbers

"""
data = [10, 501, 22, 37, 100, 999, 87, 351]
# The 'lambda x: x > 4' is a short way to define a function that checks if a number is greater than 4
result = filter(lambda x: x > 4, data)

# Print the filtered result after converting it into a list
print(list(result))


# Expected output:

[10, 501, 22, 37, 100, 999, 87, 351]


"""
Define a list containing elements of different types(integers and string)
"""
my_list = [10, 'JAY', 25, 'SHANKAR', 30, 'python']
# In this case, it checks if the element is an instance of int (for integers) or str (for strings)
check_type = lambda x: isinstance(x, int) or isinstance(x, str)

# In this case, it checks if all elements are either integers or strings
result = all(check_type(element) for element in my_list)

# Print the result
print("All elements in the list are integers or strings:", result)


"""
Generate Fibonacci series using a lambda function

"""
from functools import reduce

# Define a lambda function to generate Fibonacci series
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Generate Fibonacci series with 50 elements
result = fibonacci_series(50)

# Print the Fibonacci series
print(result)

"""
regular expression validation for various data types :

"""

import re

def validate_regex(data, regex_pattern):
    for item in data:
        yield bool(re.match(regex_pattern, item))

# Email Address
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Mobile numbers of Bangladesh
bangladesh_mobile_pattern = r'^\+?8801[3-9]\d{8}$'

# Telephone numbers of USA
usa_telephone_pattern = r'^\+?1?\s*(\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'

# 16 character Alpha-Numeric password
password_pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{16}$'

data = [
    "example@email.com",       # Email Address
    "+8801712345678",          # Mobile numbers of Bangladesh
    "+1 (123) 456-7890",      # Telephone numbers of USA
    "Password123!@#$%^&"     # 16 character Alpha-Numeric password
]

patterns = [email_pattern, bangladesh_mobile_pattern, usa_telephone_pattern, password_pattern]

for pattern, item in zip(patterns, data):
    print("Validation result:", list(validate_regex([item], pattern))[0])
