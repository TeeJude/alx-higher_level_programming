#!/bin/bash
# script that sends JSON POST request to URL passed as the first argument, displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
