import random


def generate_test_data(num_of_generated_values, lower_bound=-1000000, upper_bound=1000000, sorted_=True):
    arr = []
    for i in range(num_of_generated_values):
        n = random.randint(lower_bound, upper_bound)
        arr.append(n)
    if sorted_:
        arr.sort()
    return arr
