import multiprocessing

# Function to be executed in a process
def process_function(name):
    print(f"Process {name} starting...")
    # Perform some task in the process
    print(f"Hello from process {name}!")
    print(f"Process {name} exiting...")

if __name__ == "__main__":
    # Create multiple processes
    process1 = multiprocessing.Process(target=process_function, args=("Process 1",))
    process2 = multiprocessing.Process(target=process_function, args=("Process 2",))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to finish
    process1.join()
    process2.join()

    # Main process continues here...
    print("Main process exiting...")
