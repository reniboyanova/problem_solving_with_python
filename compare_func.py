"""
16.Function to Compute Power of Variable Arguments
Write a function that takes a variable number of arguments and returns the result of raising the first argument to the
power of the rest in order.
Input: 2, 3, 2
Output: 64 (i.e., 2^3^2 = 64)
"""


def power_of_multiple_numbers(*args):
    """
    A function that takes N numbers and raises the first number to the power of the rest in order.
    :param args: integer numbers -> example: 2, 3, 2, 4, 5
    :return: 2^3^2^4^5
    """
    if len(args) < 2:
        return "You need at least two arguments for this calculation"

    result = args[0]
    for num in args[1:]:
        result **= num

    return result


print(power_of_multiple_numbers(2, 3, 2))
