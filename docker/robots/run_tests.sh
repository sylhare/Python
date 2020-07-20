#!/usr/bin/env bash

if [[ -z "$1" ]]
then
    version="latest"
else
    version=$1
fi

docker build -t robot:latest .

docker run --rm \
           --net=host \
           -v "$PWD/output":/output \
           -v "$PWD/suites":/suites \
           -v "$PWD/scripts":/scripts \
           -v "$PWD/reports":/reports \
           --security-opt seccomp:unconfined \
           --shm-size "256M" \
           robot:${version}