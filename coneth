#!/bin/bash
command=$1
device=$2
speed=$3
duplex=$4
autoneg=$5

version="version 1.0"
help="
coneth $version
Usage :
	./coneth help --- Display help information usage

	./coneth version --- Display current version

	./coneth list --- Display list all network and device driver

	./coneth set device (speed[10:100:1000]) (duplex[half:full]) (autoneg[on:off])

	./coneth info device --- Display settings information for the specific device network

	./coneth infonet device --- Display network information for the specific device network

	./coneth dmesg device --- Display information in kernel message (dmesg)

	./coneth down device --- Down or stop running for the device network

	./coneth up device --- Up or start running for the device network

	./coneth rename device renamedDevice --- Rename the device name temporary

	./coneth speed
"

if [ $command == "help" ]; then
	echo "$help";
elif [ $command == "version" ]; then
	echo "$version";
elif [ $command == "list" ]; then
	for f in /sys/class/net/* ; do
    		dev=$(basename $f)
    		driver=$(readlink $f/device/driver/module)
    		if [ $driver ]; then
        		driver=$(basename $driver)
    		fi
    		addr=$(cat $f/address)
    		operstate=$(cat $f/operstate)
    		printf "%10s [%s]: %10s (%s)\n" "$dev" "$addr" "$driver" "$operstate"
	done;
elif [ $command == "set" ]; then
	ethtool -s $device speed $speed duplex $duplex autoneg $autoneg; 
elif [ $command == "info" ]; then
	ethtool $device | less;
elif [ $command == "infonet" ]; then
	ifconfig $device | less;
elif [ $command == "dmesg" ]; then
	dmesg | grep $device | less;
elif [ $command == "down" ]; then
	ifconfig $device down;
elif [ $command == "up" ]; then
	ifconfig $device up;
elif [ $command == "rename" ]; then
	ip link set $device name $duplex;
elif [ $command == "speed" ]; then
	speedtest;
else
	echo "coneth: bad command line arguments(s)"
	echo "For more information run coneth help"
fi
