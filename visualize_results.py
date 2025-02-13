# scripts/visualize_results.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
print("Loading processed data...")
df = pd.read_csv('data/processed/network_traffic.csv')
anomalies = pd.read_csv('data/processed/anomalies.csv')

# Plot protocol distribution
print("Plotting protocol distribution...")
sns.countplot(x='Protocol', data=df)
plt.title('Protocol Distribution')
plt.savefig('results/protocol_distribution.png')
plt.close()

# Plot packet length distribution
print("Plotting packet length distribution...")
sns.histplot(df['Length'], bins=50)
plt.title('Packet Length Distribution')
plt.savefig('results/packet_length_distribution.png')
plt.close()

# Plot anomalies
print("Plotting anomalies...")
plt.scatter(anomalies.index, anomalies['Length'], c=anomalies['Anomaly'], cmap='coolwarm')
plt.title('Network Traffic Anomalies')
plt.xlabel('Packet Index')
plt.ylabel('Packet Length')
plt.savefig('results/anomalies.png')
plt.close()

print("Visualizations saved to results/ folder.")
