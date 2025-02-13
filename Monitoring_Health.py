import psutil  # Import the psutil module to monitor system resources
import time  # Import the time module to introduce delays in monitoring

# Define the CPU usage threshold (in percentage) that triggers an alert
CPU_USAGE_THRESHOLD = 80  

def monitor_cpu_usage():
    """
    Continuously monitors the CPU usage at 1-second intervals.
    If the CPU usage exceeds the defined threshold, an alert message is displayed.
    The function runs indefinitely until interrupted by the user.
    """
    print("Monitoring CPU usage...")
    try:
        while True:
            # Get the current CPU usage percentage over a 1-second interval
            cpu_usage = psutil.cpu_percent(interval=1)

            # Check if CPU usage exceeds the threshold
            if cpu_usage > CPU_USAGE_THRESHOLD:
                print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Wait for 1 second before the next check
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C)
        print("🛑 Monitoring interrupted by user.")
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    monitor_cpu_usage()
