#!/bin/bash
# display all HTTP methods the server can accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
