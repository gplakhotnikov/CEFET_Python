import time

def measure_execution_time():
  start_time = time.time()
  for _ in range(10000):
    result = 2 + 2
  end_time = time.time()
  execution_time = end_time - start_time
  return f"Execution Time: {execution_time:.6f} seconds"

resultado = measure_execution_time()
print(resultado)