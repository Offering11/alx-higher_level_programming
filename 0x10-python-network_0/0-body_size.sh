#!/bin/bash
# send a request to an URL 
curl -s "$1" | wc -c
