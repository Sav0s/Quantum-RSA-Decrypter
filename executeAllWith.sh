#!/bin/sh

if [ ! -n "$1" ]; then
    echo "No arguments supplied"
    exit exit 1
fi

echo "Starting Script..."
python performance.py -o numeric -f "$1"
python performance.py -o qsharp -f "$1"
python performance.py -o ibmq -f "$1"
