#!/bin/bash
modprobe vcan
ip link add dev vcan0 type vcan
ip link set up vcan0
ifconfig vcan0
cd w_can/ICSim
make
./icsim vcan0
