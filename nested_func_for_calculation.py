"""
Write a function containing a nested function for addition, subtraction, multiplication and division
Input: 10, 5, "add"
Output: 15
"""


def addition(first_num: int, second_num: int) -> int:
    return first_num + second_num


def subtraction(first_num: int, second_num: int) -> int:
    return first_num - second_num


def multiplication(first_num: int, second_num: int) -> int:
    return first_num * second_num


def division(first_num: int, second_num: int) -> float:
    return first_num / second_num


def calculate_to_ints(first_num: int, second_num: int, action: str):
    if action == "add":
        return addition(first_num, second_num)
    elif action == "subtract":
        return subtraction(first_num, second_num)
    elif action == "multiply":
        return multiplication(first_num, second_num)
    elif action == "divide":
        return division(first_num, second_num)
    else:
        return "Invalid action type!"


first_number = int(input("Insert first number for calculation: "))
second_number = int(input("Insert second number for calculation: "))
action_type = input("Insert action type: ")
result = calculate_to_ints(first_number, second_number, action_type)

print(result)

