import time
import generate_random

random_array = generate_random.random_array

def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    holes = [0] * size
    for x in arr:
        holes[x - min_val] += 1
    sorted_arr = []
    for i in range(size):
        while holes[i] > 0:
            sorted_arr.append(i + min_val)
            holes[i] -= 1
    return sorted_arr

start_time = time.time()

pigeonhole_sort(random_array)

end_time = time.time()

execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {format(execution_time)} saniye")


