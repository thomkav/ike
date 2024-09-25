#!/bin/bash
set -e

# Python version - get from .python-version file
PYTHON_VERSION=$(cat .python-version)

echo "Python version: $PYTHON_VERSION"
# Get short version of Python version
PYTHON_SHORT_VERSION=$(echo $PYTHON_VERSION | cut -d '.' -f 1,2)
echo "Python short version: $PYTHON_SHORT_VERSION"

echo "Creating virtual environment ..."
# Create virtual environment
python$PYTHON_SHORT_VERSION -m venv .venv
echo "Virtual environment created."

echo "Activating virtual environment ..."
# Activate virtual environment
. .venv/bin/activate
echo "Virtual environment activated."

echo "Successfully created virtual environment."