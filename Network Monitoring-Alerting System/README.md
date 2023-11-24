Project Outline
Setup: Install necessary Python libraries (e.g., pysnmp, requests, sqlite3).

Device Configuration: Define the network devices to be monitored, including their IP addresses and SNMP or REST API credentials.

Data Collection: Write a Python script to periodically query the devices for key metrics using SNMP or REST APIs.

Database Storage: Store the collected data in a SQLite database for historical tracking and analysis.

Alerting Mechanism: Implement alerting mechanisms based on predefined thresholds or anomalies detected in the collected metrics.

# Network Monitoring and Alerting System

This system monitors network devices' health and status using SNMP (Simple Network Management Protocol) or REST APIs. It uses Python to periodically query devices for key metrics (e.g., CPU utilization, interface status) and stores the data in a SQLite database. It also implements alerting mechanisms based on predefined thresholds or anomalies detected in the collected metrics.

## Setup

1. Install necessary Python libraries: `pip install pysnmp requests sqlite3`
2. Define your network devices in the `devices` list in `monitor.py`.
3. Run the monitoring script: `python monitor.py`