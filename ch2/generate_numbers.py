import random


def generate_test_data(num_of_generated_values, sorted_=True):
    arr = []
    for i in range(num_of_generated_values):
        n = random.randint(-100000, 100000)
        arr.append(n)
    if sorted_:
        arr.sort()
    return arr
