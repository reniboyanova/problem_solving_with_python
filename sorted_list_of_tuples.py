"""
8.Lambda Function to Sort a List of Tuples
Write a lambda function that takes a list of tuples and sorts them by the second element.
Input: [(1, 2), (3, 1), (5, 0)]
Output: [(5, 0), (3, 1), (1, 2)]

"""

input_lst = [(1, 2), (3, 1), (5, 0), (4, 3), (5, 3)]
lambda_sorted_list = lambda lst: sorted(lst, key=lambda x: x[1])
sorted_output = lambda_sorted_list(input_lst)
print(sorted_output)

