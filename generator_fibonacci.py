"""
Write a generator function that yields the Fibonacci sequence up to n numbers.
Input: 5
Output: 0, 1, 1, 2, 3

"""


def fibonacci_generator(number):
    """
    A function generator of fibonacci numbers
    :param number:
    """
    current_num = 0
    next_num = 1
    for _ in range(number):
        yield current_num
        current_num, next_num = next_num, current_num + next_num


def list_printer(lst):
    """
    Print list elements, separated by coma ','
    :param lst:
    :return:
    """
    print(", ".join([str(el) for el in lst]))


n = 5
fib_sequence = list(fibonacci_generator(n))
list_printer(fib_sequence)


