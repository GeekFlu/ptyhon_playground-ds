def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits representing (x + 1)
    """
    r_arr = []
    size = len(arr)
    num = 0
    exp = size - 1
    for i in range(size):
        num += arr[i] * (10 ** exp)
        exp -= 1
    num += 1
    size = len(str(num))
    exp = size - 1
    for i in range(size):
        n_num = num // 10 ** exp
        r_arr.append(n_num)
        num = num % 10 ** exp
        exp -= 1
    return r_arr


if __name__ == "__main__":
    arr_ = [9, 9, 9, 9, 9, 9]
    print(add_one(arr_))

    arr_ = [9]
    print(add_one(arr_))

    arr_ = [0]
    print(add_one(arr_))

    arr_ = [9, 9]
    print(add_one(arr_))
