#!/bin/bash
cd ~
cd Desktop
modprobe vcan

/usr/bin/expect <<EOD
spawn sudo ip link add dev vcan0 type vcan
expect "password"
send "kali\n"
expect eof
spawn sudo ip link set up vcan0
spawn sudo ifconfig vcan0
EOD



