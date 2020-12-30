#!/bin/sh

if [ ! -n "$1" ]; then
    echo "No arguments supplied"
    exit exit 1
fi

echo "Starting Script..."
python Quantum-RSA-Decryptor/performance.py -o numeric -f "$1"
python Quantum-RSA-Decryptor/performance.py -o qsharp -f "$1"
python Quantum-RSA-Decryptor/performance.py -o ibmq -f "$1"
