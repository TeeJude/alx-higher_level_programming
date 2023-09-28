#!/bin/bash
# script that sends request to URL passed as argument, displays only the status code of the response
curl -o /dev/null -sw "%{http_code}" $1
