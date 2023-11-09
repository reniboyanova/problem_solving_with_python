"""
11.Nested Function to Calculate Exponential
Write a function containing a nested function that calculates the exponential of a number using a given base.
Input: 2, 3
Output: 8
"""


def calculate_exponential(base: int, power: int):
    """
    Calculate exponential number, by using a nested function for calculation
    :param base: every integer number
    :param power: every integer number
    :return: A result of nested function
    """
    def calculate_num_of_power(base_num: int, power_num: int) -> int:
        """
        Calculate power of number
        :param base_num:
        :param power_num:
        :return: result
        """
        return base_num ** power_num
    return calculate_num_of_power(base, power)


print(calculate_exponential(2, 3))