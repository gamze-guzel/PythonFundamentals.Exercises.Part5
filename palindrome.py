def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # pass  # remove pass statement and implement me
    if str[::1] == str[::-1]:
        return True
    else:
        return False



