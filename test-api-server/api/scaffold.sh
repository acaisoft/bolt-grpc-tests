#!/bin/bash
node_exporter &
/grpc-api &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?