# Network Inventory Management Tool

![Python](https://img.shields.io/badge/Python-3.x-blue)

This Python application leverages Nmap to scan your local network and automatically create an inventory of devices, their IP addresses, open ports, and services. The inventory data is stored in a SQLite database for easy management.

## Features

- Scans the local network using Nmap.
- Gathers information about devices, IP addresses, open ports, and services.
- Stores the inventory data in a database for easy management.

## Requirements

- Python 3.x
- Nmap (Ensure it is installed on your system and accessible in the command-line.)
- [python-nmap](https://pypi.org/project/python-nmap/) library
- [SQLite](https://www.sqlite.org/) database library (Included in Python standard library)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/n3xtchanc3/network-inventory-management.git
cd network-inventory-management

    Install the required Python libraries:

pip install python-nmap

Usage

    Customize the hosts and arguments in the perform_network_scan function in network_inventory_management.py to specify the IP address range and Nmap scan options you want to use.

    Run the Python script:

python3 network_inventory_management.py

    The script will perform an Nmap scan on the specified IP address range and gather information about devices, IP addresses, open ports, and services.

    The inventory data will be stored in a SQLite database named network_inventory.db.

Note: Ensure you have proper authorization before scanning any network. Unauthorized scanning may be illegal and unethical.
Database Schema

The application uses the following database schema to store the inventory data:

devices table
-----------------------
| id (Primary Key)     |
| ip_address (TEXT)    |
| hostname (TEXT)      |
| vendor (TEXT)        |
| open_ports (TEXT)    |
-----------------------

License

MIT License
Contributions

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.
Contact

If you have any questions or suggestions, you can contact me at your_email@example.com.
