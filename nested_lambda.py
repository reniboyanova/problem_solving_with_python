"""
Write a function that takes a number n and return a lambda function a lambda function that multiply its input by n
"""


def returning_lambda_func_with_multiplier(n: int):
    """
    Function which returns a lambda function. Keep in mind that you need to pass an argument if you want to use it
    :param n:
    :return lambda function:
    """
    return lambda number: number * n


multiply_by_2 = returning_lambda_func_with_multiplier(2)
lambda_result = multiply_by_2(10)
print(lambda_result)


