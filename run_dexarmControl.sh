#!/bin/bash

# Navigate to the directory containing dexarmControl.py

echo "#################"
echo "Script is running"
echo "#################"


cd /home/dexarm/dexarmcontroller


# Activate the virtual environment (if applicable)
# source ./venv/bin/activate


# Run the Python script
/usr/bin/python3 dexarmControl.py
