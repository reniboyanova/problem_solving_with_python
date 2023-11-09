"""
Write a function containing nested functions to perform various string manipulations like uppercase, lowercase,
and capitalization.
Input: "hello", "uppercase"
Output: "HELLO"
"""


def string_manipulation(string: str, action: str) -> str:
    """
    A function that manipulate a string by passing text and action.
    If string is not only by letters the function will return a message!
    :param string: "hello"
    :param action: "uppercase"
    :return: string after manipulation -> "HELLO"
    """
    if not string.isalpha():
        return "String is not only alphabetic!\nPlease try again!"

    if action == "uppercase":
        def make_string_uppercase():
            return string.upper()

        return make_string_uppercase()

    elif action == "lowercase":
        def make_string_lowercase():
            return string.lower()

        return make_string_lowercase()

    elif action == "capitalization":
        def make_string_capitalization():
            return string.capitalize()

        return make_string_capitalization()

    else:
        return "Invalid action!\nPlease try again!"


test_string = "hello"
action_upper = "uppercase"
action_lower = "lowercase"
action_capitalize = "capitalization"

# try function:
print(string_manipulation(test_string, action_capitalize))

# try invalid string argument:
print(string_manipulation("hell0", action_capitalize))

# try invalid action:
print(string_manipulation(test_string, "action_capitalize"))
