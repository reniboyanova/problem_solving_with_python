"""
Write a lambda function that checks if strings is palindrome ot not.
Input: madam
Output: True
"""

palindrome_checker = lambda string: string == string[::-1]

test_string = "madam"

print(palindrome_checker(test_string))
