#!/bin/bash
# script that takes in URL as an argument, sends GET request to the URL, displays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"
