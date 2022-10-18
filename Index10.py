def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a = int(s)
    x1 = a % 10
    x2 = a // 10 % 10
    x3 = a // 100 % 10
    x4 = a // 1000 % 10
    x5 = a // 10000
    return x1 + x2 + x3 + x4 + x5

print(main('12345'))