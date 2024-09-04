## phase three week one code challenge
##
Here's a fluent README file based on the provided code:

Python Coding Assessment
This repository contains Python functions that demonstrate fundamental programming concepts, including basic data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.

Functions and Classes Implemented
1. add_numbers(num1, num2)
This function takes two numbers as input and returns their sum.

Example Usage:

python
Copy code
print(add_numbers(4, 6))  # Output: 10
2. apply_decorator(func)
This is a decorator function that prints "Decorator Applied" before executing the decorated function.
Example Usage:

python
Copy code
@apply_decorator
def decoratade():
    print("Wambua")

decoratade()
Output:

Copy code
Decorator Applied
Wambua
3. calculate_factorial(n)
This function calculates the factorial of a non-negative integer n.

Example Usage:

python
Copy code
print(calculate_factorial(4))  # Output: 24
4. count_vowel(text)
This function counts the number of vowels in a given string.

Example Usage:

python
Copy code
print(count_vowel("omondi"))  # Output: 3
5. is_even(number)
This function checks if a number is even.

Example Usage:

python
Copy code
print(is_even(17))  # Output: False
6. merge_dicts(dict1, dict2)
This function merges two dictionaries, summing values for common keys.

Example Usage:

python
Copy code
word_count1 = {"python": 3, "code": 2, "data": 4}
word_count2 = {"code": 3, "openAI": 5, "python": 1}

print(merge_dicts(word_count1, word_count2))
# Output: {'python': 4, 'code': 5, 'data': 4, 'openAI': 5}
7. Car Class
This class represents a car with attributes for make, model, and year. It includes a method display_info that prints the car's details.

Example Usage:

python
Copy code
car = Car("Mercedes-Benz", "SUV", 2024)
car.display_info()
Output:

yaml
Copy code
make: Mercedes-Benz, model: SUV, year: 2024
8. reverse_string(text)
This function reverses a given string.

Example Usage:

python
Copy code
print(reverse_string("Macxwell"))  # Output: llewxcaM
9. sort_by_age(musicians)
This function sorts a list of tuples (each containing a musician's name and age) by age in ascending order.

Example Usage:

python
Copy code
musicians = [("Kendrick", 32), ("trio", 18), ("Ya levis", 27), ("Davido", 33)]
print(sort_by_age(musicians))
Output:

css
Copy code
[('trio', 18), ('Ya levis', 27), ('Kendrick', 32), ('Davido', 33)]
@macxwellomondi.