#!/bin/sh
udevd --daemon
udevadm trigger
modprobe spi-bcm2708
modprobe fbtft_device name=pitft verbose=0 rotate=270


#setterm -blank 0 -powersave off -powerdown 0
mknod /dev/fb1 c 29 1

echo "starting python script"
python /usr/src/app/stockPrice.py