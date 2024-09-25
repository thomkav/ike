#!/bin/bash
set -e

echo "Shell Script - Activating virtual environment ..."
#shellcheck disable=SC1091
. .venv/bin/activate
echo "Shell Script - Done activating virtual environment."

echo "Shell Script - Stopping the streamlit app ..."
pkill -9 -f streamlit
echo "Shell Script - Done stopping the streamlit app."