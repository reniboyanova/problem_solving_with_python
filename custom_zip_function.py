"""
8.Custom ZIP Function

Description: Implement a generator that behaves like the built-in zip function, taking two or more iterables
and returning tuples.
Example Input: [1, 2], [3, 4]
Example Output: (1, 3), (2, 4)
"""


def custom_zip_generator(*iterables):
    """
    Custom zip generator, working as same as build in 'zip()'
    :param iterables: *iterables
    :return: zipped tuples
    """
    min_length = min(len(iterable) for iterable in iterables)
    for index in range(min_length):
        yield tuple(iterable[index] for iterable in iterables)


first_lst = [1, 2]
second_lst = [3, 4]
third_lst = [5, 6, 7]
forth_lst = [1, 1, 1]

zip_iterator = custom_zip_generator(first_lst, second_lst)

zip_iterator_2 = custom_zip_generator(first_lst, second_lst, third_lst, forth_lst)

print(*zip_iterator, sep=', ')

print(*zip_iterator_2, sep=', ')

