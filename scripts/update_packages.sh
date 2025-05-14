#!/usr/bin/env bash
set -euo pipefail

echo "Running apt-get update && upgrade"
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Package update complete"
