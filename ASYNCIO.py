import asyncio

# Define an asynchronous coroutine
async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("Coroutine completed")

# Create an event loop
loop = asyncio.get_event_loop()

# Schedule the coroutine for execution in the event loop
task = loop.create_task(my_coroutine())

# Run the event loop until the task is complete
loop.run_until_complete(task)

# Close the event loop
loop.close()
