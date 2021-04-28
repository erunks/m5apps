#!/bin/bash

OS=`python3 -mplatform | grep -oE "Ubuntu|Linux|macOS"`

if [ $OS == 'macOS' ]
then
  # find the M5stack on mac
  DEV_DEVICE=`ls /dev/tty.usb* | grep -oE "tty.+"`
else
  # list /dev devices and look for the M5stack in linux
  DEV_DEVICE=`ls -l /dev/serial/by-id/ | grep "M5stack" | grep -oE "(ttyUSB.+)"`
fi

echo "/dev/$DEV_DEVICE"
