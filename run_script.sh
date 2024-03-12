#!/bin/bash

# Navigate to the directory of the script
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

# Run your Python script
python resolve_urls.py

# Optionally, deactivate the virtual environment
deactivate
