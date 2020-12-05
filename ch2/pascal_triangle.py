"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
For example,
    if n = 4, then output = [1, 4, 6, 4, 1].
To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
"""

factorial_cache = dict()


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

    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    row_coefficients = []
    factorial_row = factorial_iterative(n)
    for k in range(n + 1):
        # first and last element always are 1
        if k == 0 or k == n:
            row_coefficients.append(1)
            continue
        if factorial_cache.get(k) is not None and factorial_cache.get(n - k) is not None:
            coefficient = factorial_row / (factorial_cache.get(k) * factorial_cache.get(n - k))
        else:
            fac_nk = factorial_iterative(n - k)
            fac_k = factorial_iterative(k)
            coefficient = factorial_row / (fac_k * fac_nk)
            factorial_cache[n - k] = fac_nk
            factorial_cache[k] = fac_k
        row_coefficients.append(int(coefficient))
    return row_coefficients


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

    row_4 = nth_row_pascal(4)
    assert row_4 == [1, 4, 6, 4, 1]

    row_14 = nth_row_pascal(14)
    print(f"row(14) = {row_14}")
    assert row_14 == [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]

    row_24 = nth_row_pascal(94)
    print(f"row(24) = {row_24}")

    row_124 = nth_row_pascal(3)
    print(f"row(2) = {row_124}")
