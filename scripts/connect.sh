#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
DEV_DEVICE=$( $DIR/get_device_location.sh )

# open connection to the M5stack
`screen $DEV_DEVICE 115200`
