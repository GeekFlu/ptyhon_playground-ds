def binary_search(array, target, is_iterative=True):
    if is_iterative:
        return binary_search_iterative(array, target)
    else:
        return binary_search_recursive_sol(array, target)


def binary_search_recursive_sol(array, target):
    """Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """

    return binary_search_recursive(array, target, 0, len(array) - 1)


def binary_search_recursive(array, target, left_pointer, right_pointer):
    if array is None or len(array) <= 0:
        return -1

    if left_pointer <= right_pointer:

        mid = left_pointer + (right_pointer - left_pointer) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search_recursive(array, target, mid + 1, right_pointer)
        else:
            return binary_search_recursive(array, target, left_pointer, mid - 1)
    else:
        return -1


def binary_search_iterative(array, target):
    """
        Write a function that implements the binary search algorithm using iteration

        args:
          array: a sorted array of items of the same type
          target: the element you're searching for

        returns:
          int: the index of the target, if found, in the source
          -1: if the target is not found

        Algorithm:
            1. Find the center of the list (try setting an upper and lower bound to find the center)
            2. Check to see if the element at the center is your target.
            3. If it is, return the index.
            4. If not, is the target greater or less than that element?
            5. If greater, move the lower bound to just above the current center
            6. If less, move the upper bound to just below the current center
            7. Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
        """
    if array is None or len(array) <= 0:
        return -1

    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:
        mid = left_pointer + (right_pointer - left_pointer) // 2

        # Check if x is present at mid
        if array[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif array[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1
    return -1


def first_and_last_index(arr, number):
    # search first occurrence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)

    # search last occurrence
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)
