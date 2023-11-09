"""
15.Generator for Geometric Progression
Write a generator function that yields a geometric progression with a given start, ratio, and length.
Input: 2, 3, 4
Output: 2, 6, 18, 54
"""


def geometric_progression_generator(start: int, ratio: int, length: int):
    """
    A generator that yield a geometric progression
    :param start: integer number; example 2
    :param ratio: integer number; example 3
    :param length: integer number; example 4
    :return: result of multiplication by start and ratio, which collect in variable result; example: 2 * 3 (ratio) = 6;\
    6 * 3 (ratio) = 18... while action stop in the end of given length
    """
    result = start

    for n in range(1, length + 1):
        yield result
        result *= ratio


geometric_progression_iterator = list(geometric_progression_generator(2,3,4))
print(", ".join([str(x) for x in geometric_progression_iterator]))