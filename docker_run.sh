#!/bin/bash

if [ "$#" -eq 0 ]; then
  docker run -d -p 9999:9999 --env-file config/docker.env --name face_orientation_api \
   face_orientation_api:latest
elif [ "$#" -eq 2 ]; then
  # Process the host and port arguments
  host="$1"
  port="$2"
  docker run -d -p $port:$port --env-file config/docker.env --name face_orientation_api \
   face_orientation_api:latest --host=$host --port=$port
else
  echo "Only host and port arguments are allowed."
fi