import time
import generate_random

random_array = generate_random.random_array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

start_time = time.time()

insertion_sort(random_array)

end_time = time.time()

execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {format(execution_time)} saniye")


