"""
7.Nested Generator for Flattening Lists

Description: Create a generator that takes a nested list and flattens it.
Example Input: [[1, 2], [3, 4]]
Example Output: 1, 2, 3, 4
"""


def flatten_list_generator(nested_list):
    """
    Flatten list generator (unpacking nested lists)
    :param nested_list:
    :return:
    """
    for lst in nested_list:
        for num in lst:
            yield num


nested_list = [[1, 2], [3, 4]]
flattened_iterator = list(flatten_list_generator(nested_list))
print(", ".join([str(x) for x in flattened_iterator]))
