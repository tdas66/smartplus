import subprocess
import platform
import socket
import psutil

class SmartPlus:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.os_name = platform.system()
        self.os_version = platform.version()

    def display_system_info(self):
        print(f"Hostname: {self.hostname}")
        print(f"IP Address: {self.ip_address}")
        print(f"OS Name: {self.os_name}")
        print(f"OS Version: {self.os_version}")

    def list_network_adapters(self):
        if self.os_name == "Windows":
            command = "ipconfig"
        else:
            command = "ifconfig"
        
        print("Network Adapters:")
        subprocess.run(command, shell=True)

    def optimize_network(self):
        # Placeholder for network optimization methods
        print("Optimizing network settings...")
        # This could include adjusting TCP/IP settings, clearing DNS cache, etc.
        if self.os_name == "Windows":
            subprocess.run("ipconfig /flushdns", shell=True)
            print("DNS cache flushed.")
        else:
            print("Network optimization features are currently available for Windows only.")

    def monitor_bandwidth(self):
        print("Monitoring bandwidth usage...")
        for connection in psutil.net_connections(kind='inet'):
            print(f"PID: {connection.pid}, Local Address: {connection.laddr}, Remote Address: {connection.raddr}, Status: {connection.status}")

if __name__ == "__main__":
    smartplus = SmartPlus()
    smartplus.display_system_info()
    smartplus.list_network_adapters()
    smartplus.optimize_network()
    smartplus.monitor_bandwidth()