"""
12.Generator for Multiplication Table
Write a generator function that yields the multiplication table for a given number up to n.
Input: 3, 5
Output: 3, 6, 9, 12, 15

"""


def generator_for_multiplication_table(start_num, num_for_multiply_range):
    """
    Generator which is like a multiplication table
    :param start_num: Example: 3
    :param num_for_multiply_range: Example: 5
    :return: every step of multiplication. 3 * 1, 3 * 2, 3 * 3... while 3 * 5 (5 is end) and so on
    """
    for num in range(1, num_for_multiply_range + 1):
        result = start_num * num
        yield result


multiplication_iterator = list(generator_for_multiplication_table(3, 5))
print(', '.join([str(n) for n in multiplication_iterator]))

