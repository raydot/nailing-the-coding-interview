import time

def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {}
    
    # If we've already got the value use that 
    # instead of recomputing it (memoization)
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    # Store the result before returning
    memo[n] = result
    return result
  
def fibonacci_timer():
    test_values = [10, 20, 30, 35, 40, 45, 100, 500]

    print("Performance times:")
    print ('=' * 40)

    for n in test_values:
      start_time = time.perf_counter()
      result = fibonacci_memoized(n)
      end_time = time.perf_counter()

      total_time = end_time - start_time
      print(f"fibonacci({n}) = {result:>10} | Time: {total_time:>7.4f}s")

fibonacci_timer()