#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
ROOT=$( cd "$( dirname "$DIR" )" && pwd )
DEV_DEVICE=$( $DIR/get_device_location.sh )

export AMPY_PORT=$DEV_DEVICE

ampy put boot.py

# put entire folder contents
ampy put apps
ampy put examples
ampy put utils

# put specific files
ampy mkdir external_modules
ampy put external_modules/abutton.py external_modules/abutton.py
ampy put external_modules/font.py external_modules/font.py
ampy put external_modules/mpu6886.py external_modules/mpu6886.py
