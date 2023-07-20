#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Apply database migrations using Aerich
echo "Apply database migrations"
aerich upgrade

# Start the application
echo "Starting the application"
uvicorn run:app --host 0.0.0.0 --port 8080 --reload
