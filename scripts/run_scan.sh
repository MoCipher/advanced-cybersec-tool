#!/bin/bash

# This script automates the process of running a scan for the advanced cybersecurity tool.

# Load configuration settings
source ../src/config.py

# Check if required tools are installed
if ! command -v nmap &> /dev/null; then
    echo "Nmap could not be found. Please install Nmap to proceed."
    exit 1
fi

if ! python3 -c "import scapy" &> /dev/null; then
    echo "Scapy could not be found. Please install Scapy to proceed."
    exit 1
fi

# Set up the environment
echo "Setting up the environment..."
# (Add any environment setup commands here)

# Run the network scan using the Scanner class
echo "Starting network scan..."
python3 ../src/main.py --scan-type network

# Run vulnerability assessment
echo "Starting vulnerability assessment..."
python3 ../src/main.py --scan-type vulnerability

echo "Scan completed. Check the output for results."