#!/bin/sh
udevd --daemon
udevadm trigger
modprobe spi-bcm2708
modprobe fbtft_device name=pitft verbose=0 rotate=270


echo "starting python script"
python /usr/src/app/stockPrice.py