def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    i = 0
    count = 0

    while i < len(s):
        if s[i].isdigit():
            count += 1
        i += 1
    return count