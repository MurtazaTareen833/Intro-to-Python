import time

# Get the current time
current_time = time.time()
print("Current Time:", current_time)

# Pause the program for 2 seconds
print("Pausing for 2 seconds...")
time.sleep(2)
print("Resuming...")

# Measure the time taken for a code block to execute
start_time = time.time()

# Perform some time-consuming task
for i in range(1000000):
    pass

end_time = time.time()

execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")
