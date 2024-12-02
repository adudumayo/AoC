import time

# Start the timer
start_time = time.time()

# Code block to be timed
# Example: a simple loop
for i in range(1000000):
    pass

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
