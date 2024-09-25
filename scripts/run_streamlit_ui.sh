#!/bin/bash
set -e

echo "Shell Script - Activating virtual environment ..."
#shellcheck disable=SC1091
. .venv/bin/activate
echo "Shell Script - Done activating virtual environment."

echo "Shell Script - Running the streamlit app ..."
streamlit run streamlit_ui.py
echo "Shell Script - Done running the streamlit app."