#!/bin/sh
udevd --daemon
udevadm trigger

if [ ! -c /dev/fb1 ]; then
  modprobe spi-bcm2708
  modprobe fbtft_device name=pitft verbose=0 rotate=270

  sleep 1

  mknod /dev/fb1 c $(cat /sys/class/graphics/fb1/dev | tr ':' ' ')
fi

echo "starting python script"
python /usr/src/app/stockPrice.py