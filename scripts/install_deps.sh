#!/bin/bash

# Update package list and install necessary dependencies
sudo apt-get update

# Install Nmap
sudo apt-get install -y nmap

# Install Python dependencies
pip install -r ../requirements.txt

# Install Scapy
pip install scapy

# Additional dependencies can be added here
echo "All dependencies have been installed."