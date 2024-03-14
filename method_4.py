import time
import generate_random

random_array = generate_random.random_array

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(pivot)
    return quick_sort(left) + middle + quick_sort(right)

start_time = time.time()

quick_sort(random_array)

end_time = time.time()

execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {format(execution_time)} saniye")


