#!/bin/bash
set -e

# Check if .venv directory exists
if [ ! -d ".venv" ]; then
    echo "The .venv directory doesn't exist. Please create it before running this script."
    exit 1
fi

echo "Shell Script - Activating virtual environment ..."
#shellcheck disable=SC1091
. .venv/bin/activate
echo "Shell Script - Done activating virtual environment."

echo "Shell Script - Locking dependencies using poetry ..."
poetry lock
echo "Shell Script - Done locking dependencies."

echo "Shell Script - Installing dependencies using poetry ..."
poetry config virtualenvs.in-project true
poetry install --no-interaction --no-ansi --no-root --without dev
echo "Shell Script - Done installing dependencies."