#!/bin/bash
# sends a JSON POST request to a URL, to show the responds
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
