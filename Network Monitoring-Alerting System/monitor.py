# Step 1: Setup
# Install necessary libraries with pip
# pip install pysnmp requests sqlite3

# Step 2: Device Configuration
devices = [
    {"ip": "192.168.1.1", "community": "public", "version": "2c"},
    # Add more devices as needed
]

# Step 3: Data Collection
from pysnmp.hlapi import *

for device in devices:
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(device["community"], mpModel=1),
               UdpTransportTarget((device["ip"], 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

# Step 4: Database Storage
# This is a simplified example. In a real-world application, you'd want to use a database ORM like SQLAlchemy.
import sqlite3
conn = sqlite3.connect('network_monitor.db')
c = conn.cursor()
c.execute('''CREATE TABLE metrics
             (date text, ip text, metric text, value real)''')

# Step 5: Alerting Mechanism
# This is a very basic example. You'd want to implement more sophisticated alerting logic.
def check_threshold(ip, metric, value):
    if metric == "cpu" and value > 90:
        print(f"ALERT: CPU usage on {ip} is over 90%!")