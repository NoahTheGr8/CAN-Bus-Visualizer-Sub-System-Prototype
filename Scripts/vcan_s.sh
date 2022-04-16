#!/bin/bash
cd ~
modprobe vcan
ip link add dev vcan0 type vcan
ip link set up vcan0
ifconfig vcan0
