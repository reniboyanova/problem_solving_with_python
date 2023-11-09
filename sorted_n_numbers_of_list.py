"""
17.Function to Sort Variable Number of Lists
Write a function that takes a variable number of lists and returns a single list containing all the elements, sorted.
Input: [3, 1], [5, 2], [4, 0]
Output: [0, 1, 2, 3, 4, 5]
"""


def sort_numbers_in_lists(*args):
    """
    A function that takes N number of lists with integers and return one sorted list in ascending order
    :param args: [3, 1], [5, 2], [4, 0]
    :return: [0, 1, 2, 3, 4, 5]
    """
    lst = []

    for num_lst in args:
        while num_lst:
            lst.append(num_lst.pop())

    return sorted(lst)


print(sort_numbers_in_lists([3, 1], [5, 2], [4, 0]))