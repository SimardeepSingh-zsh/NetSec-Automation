from scapy.all import sniff, IP, TCP
from matplotlib import pyplot as plt
import time

# Initialize a dictionary to hold packet counts
packet_counts = {}
syn_counts = {}

def handle_packet(packet):
    # Only handle IP packets
    if IP in packet:
        # Get the current time
        current_time = time.time()
        
        # If the current time is not in the dictionary, add it with a count of 1
        if current_time not in packet_counts:
            packet_counts[current_time] = 1
        else:
            # If the current time is already in the dictionary, increment the count
            packet_counts[current_time] += 1

        # Check for SYN flags in TCP packets
        if TCP in packet and packet[TCP].flags == 'S':
            syn_key = (packet[IP].src, packet[IP].dst)
            if syn_key not in syn_counts:
                syn_counts[syn_key] = 1
            else:
                syn_counts[syn_key] += 1

# Sniff the network
sniff(prn=handle_packet)

# Create lists for the x and y values of the plot
x_values = list(packet_counts.keys())
y_values = list(packet_counts.values())

# Create the plot
plt.plot(x_values, y_values)

# Show the plot
plt.show()

# Print potential SYN flood attacks
for syn_key in syn_counts:
    if syn_counts[syn_key] > 100:
        print(f"Potential SYN flood attack detected from {syn_key[0]} to {syn_key[1]}")