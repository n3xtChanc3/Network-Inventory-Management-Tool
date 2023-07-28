import nmap
import sqlite3

# Function to perform Nmap scan on the local network
def perform_network_scan():
    nm = nmap.PortScanner()
    nm.scan(hosts="192.168.0.1/24", arguments="-F")  # Customize the hosts and scan arguments as needed
    return nm.all_hosts()

# Function to extract device information from the Nmap scan results
def extract_device_info(hosts):
    devices = []
    for host in hosts:
        device = {
            "ip_address": host,
            "hostname": nm[host].hostname(),
            "vendor": nm[host].vendor(),
            "open_ports": nm[host]["tcp"].keys(),
        }
        devices.append(device)
    return devices

# Function to create and populate the SQLite database with the inventory data
def create_database(devices):
    conn = sqlite3.connect("network_inventory.db")  # Create or connect to the SQLite database
    cursor = conn.cursor()

    # Create the table for devices in the database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT NOT NULL,
            hostname TEXT,
            vendor TEXT,
            open_ports TEXT
        )
    """)

    # Insert device information into the database
    for device in devices:
        cursor.execute("""
            INSERT INTO devices (ip_address, hostname, vendor, open_ports)
            VALUES (?, ?, ?, ?)
        """, (device["ip_address"], device["hostname"], device["vendor"], ",".join(str(port) for port in device["open_ports"])))

    # Commit changes and close the database connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    hosts = perform_network_scan()
    devices = extract_device_info(hosts)
    create_database(devices)
    print("Network Inventory has been created and stored in network_inventory.db.")
