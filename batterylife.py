import psutil
import subprocess


def get_battery_life():
    # Get battery information
    battery = psutil.sensors_battery()

    # Print battery status and life, and display notification if below threshold
    if battery is not None:
        status = battery.power_plugged
        percent = battery.percent
        if status:
            status_text = "Charging"
            print(f"Battery status: {status_text} ({percent}%)")
        else:
            status_text = "On Battery Power"
            print(f"Battery status: {status_text} ({percent}%)")
            threshold = 20  # percent
            if percent < threshold:
                notification_text = f"Battery life is below {threshold}%!"
                print(notification_text)
                subprocess.run(["osascript", "-e", f"display notification \"{notification_text}\""])
    else:
        print("Battery information not available.")

# Call the function to get and print the battery life
get_battery_life()
