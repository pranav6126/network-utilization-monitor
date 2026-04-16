import subprocess
import time

while True:
    print("===== Network Utilization =====")
    output = subprocess.check_output("ip -s link", shell=True).decode()
    print(output)
    time.sleep(3)
