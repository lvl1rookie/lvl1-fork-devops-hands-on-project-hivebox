from time import perf_counter

def my_print(message):
    print("(Semantic Versioning v0.0.1)")
    print("-------------------------------")
    print(message)
    print("-------------------------------")

def delay(seconds):
    start = perf_counter()
    while perf_counter() - start < seconds:
        pass  # Wait in real time

# Example usage
my_print("Program is done running")

# Wait for 5 seconds in real time
delay(2)