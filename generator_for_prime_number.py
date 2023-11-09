"""
Write a generator function that yields prime numbers up to n
Input: 10
Output: 2, 3, 5, 7
"""


def prime_checker(num: int) -> bool:
    """
    Function that check if number is prime and return bool
    :param num:
    :return True or False:
    """
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def prime_number_generator(number: int):
    for n in range(2, number + 1):
        if prime_checker(n):
            yield n


num = int(input("Please, insert a number to to check: "))

prime_iterator = list(prime_number_generator(num))

print(', '.join([str(n) for n in prime_iterator]))
