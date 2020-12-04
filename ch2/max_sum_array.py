def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


if __name__ == "__main__":
    arr = [1, 2, 3, -4, 6]
    solution = 8
    print(max_subarray(arr))
    assert max_subarray(arr) == solution

    arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
    # EYE check 408 956 0731

    solution = 18
    print(max_subarray(arr))
    assert max_subarray(arr) == solution
