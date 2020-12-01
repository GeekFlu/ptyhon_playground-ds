import random


def generate_test_data(num_of_generated_values):
    arr = []
    for i in range(num_of_generated_values):
        n = random.randint(-10000, 10000)
        arr.append(n)
    arr.sort()
    return arr
