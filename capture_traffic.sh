#!/bin/bash

# Script to capture network traffic
echo "Starting network traffic capture..."
sudo tcpdump -c 1000 -w data/raw/network_traffic.pcap
echo "Traffic capture complete. Saved to data/raw/network_traffic.pcap."
