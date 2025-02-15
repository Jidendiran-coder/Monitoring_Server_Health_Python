'''
MIT License

Copyright (c) 2025 [Jidendiran]

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the Software), to deal 
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


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
