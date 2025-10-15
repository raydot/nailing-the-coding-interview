import time

def fibonacci(n):
    if n <= 0: # There are no negative fibonacci numbers
        return 0
    elif n == 1: # First number in sequence, no recursion needed
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursion!

def fibonacci_timer():
    test_values = [10, 20, 30, 35, 40, 45]

    print("Performance times:")
    print ('=' * 40)

    for n in test_values:
      start_time = time.perf_counter()
      result = fibonacci(n)
      end_time = time.perf_counter()

      total_time = end_time - start_time
      print(f"fibonacci({n}) = {result:>10} | Time: {total_time:>7.4f}s")

fibonacci_timer()