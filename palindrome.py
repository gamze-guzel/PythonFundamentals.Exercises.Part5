def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # pass  # remove pass statement and implement me
    # if value == value[::-1]:
    #     value= value.replace(" ", " ").lower()
    #     return True
    # else:
    #     return False

    value = value.lower().replace(' ', ' ')
    return value == value[::-1]

