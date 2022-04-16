# CAN-Bus-Visualizer-Sub-System-Prototype
This repository contains a technical prototype for a sub-system within the CAN-Bus Visualizer System.

## About
This project's main purpose is to view the CAN Bus traffic in real time, replay packets, and potentially edit packets of interest by the analyst. 

## How to Get Started
1. Clone main repository
```
git clone https://github.com/NoahTheGr8/CAN-Bus-Visualizer-Sub-System-Prototype.git
```
2. Create a new branch:
```
git checkout -b <branch_name>
```
3. Push files to new branch:
```
git add .
git push origin <branch_name>
```

## How to Use
To access the main program, run 'Controller.py'. Once started, open two separate terminals. In one, navigate to the ICSim folder from the CAN-Utils workshop and use the command:
```./icsim vcan0```
From here, you can send individual packets to the CAN Bus:
```
cansend vcan0 188#01000000
cansend vcan0 244#0000000B87
```
Upon doing so, the Traffic Displayer Interface will add the packet to the table of all received packets within that session.