#!/bin/bash
for f in /sys/class/net/*; do
    dev=$(basename $f)
    echo "$dev"
done
