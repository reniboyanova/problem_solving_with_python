"""
10.Lambda Function to Filter Even Numbers
Write a lambda function that filters even numbers from a given list.
Input: [1, 2, 3, 4, 5]
Output: [2, 4]
"""

input_list = [1, 2, 3, 4, 5]
output_list = (lambda lst: [x for x in lst if x % 2 == 0])(input_list)
print(output_list)


