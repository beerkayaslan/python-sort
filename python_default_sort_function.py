import time
import generate_random

random_array = generate_random.random_array

start_time = time.time()

random_array.sort()

end_time = time.time()

execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {format(execution_time)} saniye")