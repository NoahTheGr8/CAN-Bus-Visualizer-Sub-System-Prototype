#!/bin/bash
cd ~
for i in {1..25}
do
	cansend vcan0 123#DEADBEEF
done