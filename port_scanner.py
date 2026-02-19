"""
Port scanning module for Advanced Cybersecurity Tool.
"""

import socket

def scan_ports(host, start_port, end_port):
    """
    Scan a range of ports on a given host and print open ports.
    Args:
        host (str): Target hostname or IP address.
        start_port (int): Starting port number.
        end_port (int): Ending port number.
    """
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((host, port))
                print(f"Port {port}: OPEN")
            except (socket.timeout, ConnectionRefusedError):
                # Port is closed or not responding
                pass
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
