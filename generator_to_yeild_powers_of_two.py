"""
9.Generator to Yield Powers of Two
Write a generator function that yields the powers of two up to n.
Input: 4
Output: 1, 2, 4, 8
"""


def generator_power_of_number_up_to(num):
    power = 1
    for n in range(num):
        yield power
        power *= 2


input_number = int(input("Insert a end point number: "))
powers_iterator = list(generator_power_of_number_up_to(input_number))

print(', '.join([str(number) for number in powers_iterator]))


