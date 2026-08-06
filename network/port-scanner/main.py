import socket
import os
import json
import threading
from concurrent.futures import ThreadPoolExecutor

script_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(script_dir, "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

target_ip = config.get("target_ip", "auto")
if target_ip.lower() == "auto":
    host_name = socket.gethostname()
    target_ip = socket.gethostbyname(host_name)

start_port = config.get("start_port", 1)
end_port = config.get("end_port", 65535)
timeout = config.get("timeout", 0.1)
max_threads = config.get("max_threads", 1000)
output_filename = config.get("output_file", "scan_results.txt")

open_ports = []
close_ports = []
lock = threading.Lock()

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target_ip, port))
    sock.close()

    with lock:
        if result == 0:
            open_ports.append(port)
        elif result in (10035, 10061):
            close_ports.append(port)

print(f"Scanning target {target_ip} from port {start_port} to {end_port}...")

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

output_path = os.path.join(script_dir, output_filename)
with open(output_path, "w") as f:
    f.write(f"Target IP: {target_ip}\n")
    f.write(f"Open Ports: {sorted(open_ports)}\n")
    f.write(f"Closed Ports: {sorted(close_ports)}\n")

print(f"Scan complete. Results saved to {output_filename}")