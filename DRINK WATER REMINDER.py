import time
import platform
import subprocess

def play_notification_sound():
    if platform.system() == 'Windows':
        # For Windows, use the 'win32' module to play a beep sound
        import winsound
        winsound.Beep(20000, 20000)  # Play a beep sound for 20 second
    else:
        # For other platforms, use the 'subprocess' module to invoke the system's default audio player
        subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'])

def drink_water_reminder(interval, total_duration):
    start_time = time.time()
    end_time = start_time + total_duration

    while time.time() < end_time:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"[{current_time}] It's time to drink water!")
        play_notification_sound()

        time.sleep(interval * 60)  # Convert interval from minutes to seconds

    print("Reminder completed.")

# Example usage
reminder_interval = 30  # Interval in minutes
reminder_duration = 2 * 60  # Duration in minutes

drink_water_reminder(reminder_interval, reminder_duration)
