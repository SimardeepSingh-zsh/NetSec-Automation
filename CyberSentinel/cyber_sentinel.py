import json
import requests

class ThreatDetection:
    def __init__(self):
        self.threat_feeds = [
            'https://api.threatfeed.com/indicators',
            'https://api.openthreatexchange.org/indicators',
            # Add more threat intelligence feeds here
        ]

    def fetch_threat_data(self):
        all_threat_data = []
        for feed in self.threat_feeds:
            response = requests.get(feed)
            if response.status_code == 200:
                threat_data = response.json()
                all_threat_data.extend(threat_data)
        return all_threat_data

    def analyze_threat_data(self, threat_data):
        potential_threats = []
        # Example: Check if any IP address matches known malicious IPs
        malicious_ips = self.load_malicious_ips()
        for entry in threat_data:
            if entry['type'] == 'IP':
                if entry['value'] in malicious_ips:
                    potential_threats.append(entry)
        return potential_threats

    def load_malicious_ips(self):
        # Example: Load malicious IPs from a file or database
        with open('malicious_ips.txt', 'r') as file:
            malicious_ips = file.read().splitlines()
        return malicious_ips

if __name__ == "__main__":
    threat_detection = ThreatDetection()
    threat_data = threat_detection.fetch_threat_data()
    potential_threats = threat_detection.analyze_threat_data(threat_data)
    if potential_threats:
        print("Potential threats detected:")
        for threat in potential_threats:
            print(threat)
    else:
        print("No potential threats detected.")
