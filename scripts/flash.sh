#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
DEV_DEVICE=$( $DIR/get_device_location.sh )

python3 -m esptool --port $DEV_DEVICE erase_flash
python3 -m esptool --chip esp32 --port $DEV_DEVICE write_flash -z 0x1000 esp32.bin
