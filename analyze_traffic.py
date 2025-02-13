# scripts/analyze_traffic.py
from scapy.all import rdpcap, TCP, UDP, IP
import pandas as pd
from sklearn.ensemble import IsolationForest

# Read the pcap file
print("Reading network traffic data...")
packets = rdpcap('data/raw/network_traffic.pcap')

# Extract relevant data
data = []
for packet in packets:
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)
        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        else:
            sport = None
            dport = None
        data.append([src_ip, dst_ip, protocol, sport, dport, length])

# Convert to a DataFrame
df = pd.DataFrame(data, columns=['Source_IP', 'Destination_IP', 'Protocol', 'Source_Port', 'Destination_Port', 'Length'])

# Save to CSV for further analysis
df.to_csv('data/processed/network_traffic.csv', index=False)
print("Processed data saved to data/processed/network_traffic.csv.")

# Anomaly detection
print("Performing anomaly detection...")
model = IsolationForest(contamination=0.05)
df['Anomaly'] = model.fit_predict(df[['Length']])

# Save results
df.to_csv('data/processed/anomalies.csv', index=False)
print("Anomaly detection complete. Results saved to data/processed/anomalies.csv.")
