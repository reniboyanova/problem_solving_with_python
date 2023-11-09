"""
11.Writing a Password Strength Checker Function

Description: Write a function to check the strength of a password based on criteria like length,
use of special characters, etc.
Example Input: “P@ssw0rd123”
Example Output: “Strong”
"""

import re

password = "P@ssw0rd123"


def password_checker(password_input: str) -> bool:
    """
    Password checker with using regular expression.
    Its check if password contains at least 8 or less than 32 symbols.
    For correct password is need to have len(password) >= 8 and len(password) <= 32;
    Min one lower, one capitalize, one digit and one special symbol from allowed symbol - _ . @
    :param password_input: string password
    :return: bool (True or False)
    """
    correct_password = False
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[-_\.@])(?=.*\d).+$'
    if len(password_input) < 8 or len(password_input) > 32:
        print("Your password need to be at least 8 symbols and not more than 32 symbols!")
        return False
    if re.match(pattern, password_input):
        print("This password is strong!")
        correct_password = True
    else:
        print("Your password need to contain at least:\nOne digit; One low letter; One capital letter;"
              " One special symbol from (._-@)")
        correct_password = False
    return correct_password


have_a_correct_password = True

while have_a_correct_password:
    password_to_check = input("Please insert your password: ")
    if password_checker(password_to_check):
        break





