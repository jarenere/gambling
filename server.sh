#!/bin/bash

function get_pid {
   PID=`pgrep gunicorn`
}

stop() {
   get_pid
   if [ -z $PID ]; then
      echo "server is not running."
   else
      echo -n "Stopping server.."
      kill -9 $PID
      sleep 1
      echo ".. Done."
   fi
}


start() {
   get_pid
   if [ -z $PID ]; then
      echo  "Starting server.."
      source flask/bin/activate
      gunicorn -b 0.0.0.0:5678 app:app &
      get_pid
      echo "Done. PID=$PID"
      deactivate
   else
      echo "server is already running, PID=$PID"
   fi
}

# call arguments verbatim:
$@