def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    expected_sum = 0
    current_sum = 0
    n = len(arr)
    for i in range(n):
        current_sum += arr[i]
        if i <= n - 2:
            expected_sum += i

    return current_sum - expected_sum


def duplicate_number_arithmetic_progression(arr):
    """
    Arithmetic progression:
    n(a1 + an)/ 2 since a1 is always zero
    m = n -1
    (m * an)/2

    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    expected_sum = 0
    current_sum = 0
    n = len(arr)
    for i in range(n):
        current_sum += arr[i]

    expected_sum = ((n - 1) * (n - 2)) // 2

    return current_sum - expected_sum


if __name__ == "__main__":
    arr_ = [0, 2, 3, 1, 4, 5, 3]
    solution = 3
    print(duplicate_number(arr_))
    assert solution == duplicate_number(arr_)

    arr_ = [0, 0]
    solution = 0
    assert solution == duplicate_number(arr_)

    arr_ = [0, 1, 5, 4, 3, 2, 0]
    solution = 0
    assert solution == duplicate_number(arr_)

    arr_ = [0, 1, 5, 5, 3, 2, 4]
    solution = 5
    assert solution == duplicate_number_arithmetic_progression(arr_)

    arr_ = [0, 1, 5, 4, 3, 2, 0]
    solution = 0
    assert solution == duplicate_number_arithmetic_progression(arr_)
