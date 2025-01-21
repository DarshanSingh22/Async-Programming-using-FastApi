import time
import threading

# Recursive Fibonacci function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to call the Fibonacci function and measure execution time
def call_and_measure(fib_func, n):
    start_time = time.time()
    result = fib_func(n)
    end_time = time.time()
    print(f"Fibonacci({n}) = {result} | Time taken: {end_time - start_time:.6f} seconds")

# Function to run the Fibonacci function in a separate thread
def run_in_thread(fib_func, n):
    thread = threading.Thread(target=call_and_measure, args=(fib_func, n))
    thread.start()
    return thread

# Main function
def main():
    n = 35  # Change the value of n as needed
    print(f"Calling Fibonacci recursive function for n = {n} in separate thread\n")

    # Create a list to store the threads
    threads = []
    
    # Run Fibonacci recursive function in a separate thread
    threads.append(run_in_thread(fibonacci_recursive, n))
    threads.append(run_in_thread(fibonacci_recursive, n))
    threads.append(run_in_thread(fibonacci_recursive, n))

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def main_sequential():
    n = 35  # Change the value of n as needed
    print(f"Calling Fibonacci recursive function for n = {n} in separate thread\n")

    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    print(f"\nTime taken 1: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    print(f"\nTime taken 2: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    print(f"\nTime taken 3: {end_time - start_time:.6f} seconds")



if __name__ == "__main__":
    start_time = time.time()
    main_sequential()
    end_time = time.time()
    print(f"\nTime taken: {end_time - start_time:.6f} seconds")



    