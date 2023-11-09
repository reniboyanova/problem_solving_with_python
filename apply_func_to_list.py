"""
13.Lambda Function to Apply Function to List
Write a lambda function that takes another function and a list and applies the function to every element of the list.
Input: lambda x: x*2, [1, 2, 3]
Output: [2, 4, 6]
"""

apply_function = lambda predicate_func, lst: [predicate_func(x) for x in lst]

# first predicate func:
predicate_function = lambda x: x * 2

# second predicate func:
predicate_function_2 = lambda x: x ** 2

input_list = [1, 2, 3, 4, 5]

output_list = apply_function(predicate_function, input_list)
print(output_list)

output_list = apply_function(predicate_function_2, input_list)
print(output_list)

