"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
For example,
    if n = 4, then output = [1, 4, 6, 4, 1].
To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
"""


def factorial_iterative(n):
    """
    Calculates the factorial of a given n integer
    :param n: integer
    :return: the factorial of n
    """
    if n < 0:
        raise ValueError("n cannot be less than zero 0")

    if n == 0 or n == 1:
        return 1

    fact_ = 1
    while n > 0:
        fact_ = fact_ * n
        n -= 1

    return fact_


def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle

    'n choose k' = n! / (k! * (n - k)!)
    """


if __name__ == "__main__":
    fact_n = factorial_iterative(8)
    print(f"factorial(8) = {fact_n}")

    fact_n = factorial_iterative(5)
    print(f"factorial(5) = {fact_n}")

    fact_n = factorial_iterative(10)
    print(f"factorial(10) = {fact_n}")

    fact_n = factorial_iterative(19)
    print(f"factorial(19) = {fact_n}")

    fact_n = factorial_iterative(29)
    print(f"factorial(29) = {fact_n}")

    fact_n = factorial_iterative(0)
    print(f"factorial(0) = {fact_n}")

    fact_n = factorial_iterative(1)
    print(f"factorial(1) = {fact_n}")
