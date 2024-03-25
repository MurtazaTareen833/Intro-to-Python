import threading

# Function to be executed in a thread
def thread_function(name):
    print(f"Thread {name} starting...")
    # Perform some task in the thread
    print(f"Hello from thread {name}!")
    print(f"Thread {name} exiting...")

# Create multiple threads
thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Main thread continues here...
print("Main thread exiting...")
