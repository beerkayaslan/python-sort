import time
import generate_random

random_array = generate_random.random_array

def method_1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

start_time = time.time()

method_1(random_array)

end_time = time.time()

execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {format(execution_time)} saniye")


