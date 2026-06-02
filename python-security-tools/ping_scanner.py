import os
import platform

def check_network():
    print("Starting Network Scanner...")
    # Use '-c 1' for Mac/Linux and '-n 1' for Windows
    param = '-c' if platform.system().lower() != 'windows' else '-n 1'

    # This tests your local home router IP (standard default)
    target_ip = "192.168.1.1"
    response = os.system(f"ping {param} {target_ip} > /dev/null 2>&1")

    if response == 0:
        print(f"✅ SUCCESS: Device {target_ip} is ONLINE.")
    else:
        print(f"⚠️ ALERT: Device {target_ip} is OFFLINE or unreachable.")

check_network()