# Network Traffic Analysis and Visualization

This project uses Python and libraries like Scapy and Matplotlib to capture and analyze network traffic, and visualize this data in a meaningful way.

## Features

- Capture packets in real time
- Parse packets for IP addresses and TCP flags
- Plot the number of packets per second
- Detect potential SYN flood attacks

## Requirements

- Python 3
- Scapy
- Matplotlib

## Usage

Run the script with root privileges:

```bash
sudo python3 script.py

License
MIT


Please note that running this script requires root privileges, as capturing packets is a privileged operation. Also, you need to install the required libraries using pip:

```bash
pip install scapy matplotlib