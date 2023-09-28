#!/bin/bash
# script that makes request to 0.0.0.0:5000/catch_me that causes the server to respond with You got me! message in the body of the response.
curl -sL -X PUT -H "You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
