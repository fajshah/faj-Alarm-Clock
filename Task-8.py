import datetime
import time
from playsound import playsound

def set_alarm(alarm_time, sound_file):
    try:
        # Handle both 12-hour and 24-hour formats
        if "AM" in alarm_time.upper() or "PM" in alarm_time.upper():
            parsed_time = datetime.datetime.strptime(alarm_time, "%I:%M %p")
        else:
            parsed_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format! Please enter time in HH:MM:SS or HH:MM AM/PM format.")
        return

    alarm_time_str = parsed_time.strftime("%H:%M:%S")
    print(f"Alarm set for {alarm_time_str}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            print("Wake up! It's time!")
            try:
                playsound(sound_file)
            except Exception as e:
                print(f"Error playing sound: {e}")
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (e.g., HH:MM:SS or HH:MM AM/PM): ")
    set_alarm(alarm_time, "E:/Alarm Clock/WhatsApp Audio 2025-03-12 at 3.02.31 PM.mpeg")

