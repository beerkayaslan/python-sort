import random

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

array_size = 10000
min_value = 0
max_value = 1000
random_array = generate_random_array(array_size, min_value, max_value)