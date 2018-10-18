#!/bin/bash

look_firefox=""
look_firefox=`pgrep firefox`

if [ ! -z "$look_firefox" ]
  then
    echo "Firefox found"
    sleep 30s
    pkill firefox
  fi
