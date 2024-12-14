import time

def time_complexity(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@time_complexity
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i  # i^2
    return total

result = sum_of_squares(10000)
print(f"Sum of squares: {result}")
