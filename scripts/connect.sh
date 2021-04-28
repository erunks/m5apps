#!/bin/bash

# list /dev devices and look for the M5stack
DEV_DEVICE=`ls -l /dev/serial/by-id/ | grep "M5stack" | grep -oE "(ttyUSB.+)"`

# open connection to the M5stack
`screen /dev/$DEV_DEVICE 115200`
