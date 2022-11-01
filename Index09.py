def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    answer = -1
    d = int(s)
    if  s.isdigit():
        answer = d

    return answer