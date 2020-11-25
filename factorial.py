def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i = i + 1
        n = output


if __name__ == '__main__':
    # Test block
    my_gen = fact_gen()
    num = 5
    for i in range(num):
        print(next(my_gen))

    # Correct result when num = 5:
    # 1
    # 2
    # 6
    # 24
    # 120
