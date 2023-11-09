"""
Write a function that contains a nested function to calculate the factorial of a number.
Input: 5
Output: 120
"""

# I am not sure how to make it nested this short function?

def calculate_factorial(number):
    """
    Function to calculate a factorial
    :param number:
    :return factorial:
    """
    factorial = 1

    for num in range(1, number + 1):
        factorial *= num

    return factorial


print(calculate_factorial(5))