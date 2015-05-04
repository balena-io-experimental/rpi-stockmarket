#!/bin/bash

if [ "$INITSYSTEM" = "on" ]; then
	echo Systemd init system enabled:
	env > /etc/docker.env

	echo -e "#!/bin/bash\n exec $@" > /etc/resinApp.cmd
	chmod +x /etc/resinApp.cmd

	echo 'ForwardToConsole=yes' >> /etc/systemd/journald.conf

	#udevadm trigger

	systemctl enable /etc/systemd/system/launch.service
	alias resin-app-logs='journalctl -u launch'

	#systemctl enable /etc/systemd/system/udev-trigger.service

	exec /sbin/init
else
	echo $PATH
	CMD=$(which $1)
	shift
	exec "$CMD" "$@"
fi