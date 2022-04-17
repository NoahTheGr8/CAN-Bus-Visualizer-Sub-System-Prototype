# CAN-Bus-Visualizer-Sub-System-Prototype
This repository contains a technical prototype for a sub-system within the CAN-Bus Visualizer System.

## About this program's functionality
This project's main purpose is to view the CAN Bus traffic in real time, replay packets, and edit packets of interest by the analyst.

## Status of the implementation
The status of the implementation...

## What we learned
We learned that...

## Prerequisites/Assumptions
* Kali Linux 
* Python 3.9+
* You follow these instructions **EXACTLY** as they are (scripts won't work since they depend on certain directory calls)

## How to Get Started
1. Open Kali Linux
2. Open a terminal/command prompt
3. Download the dependencies
```
sudo apt install can-utils
sudo apt install libsdl2-dev libsdl2-image-dev -y
sudo apt install python3-pip
pip install python-can
```
4. Navigate to the desktop
```
cd ~/Desktop
```
5. Clone this repository to the **Desktop**
```
git clone https://github.com/NoahTheGr8/CAN-Bus-Visualizer-Sub-System-Prototype.git
```
6. Create another folder called "w_can" on the **Desktop**
```
mkdir w_can
```
7. Navigate into the folder w_can 
```
cd ~/Desktop/w_can
```
8. Clone the simulator repository into the folder **w_can**
```
git clone https://github.com/zombieCraig/ICSim.git
```
9. Navigate to folder where the CAN Bus Visualizer System is
```
cd ../CAN-Bus-Visualizer-Sub-System-Prototype
```
10. Go into the scripts directory and load the virtual CAN module, set up virtual interface, and ensure its up and running
```
cd Scripts
./vcan_s.sh
```
11. Enter your password (probably "kali")
12. Go back a directory and start the program using the below commands below - 
```
cd ..
python3 Controller.py
```
13. Enjoy (hopefully) :)

## How to use the prototype
* Look at it and see all packets being sent on the CAN Bus
* Right-click a packet (represented as a row) and choose to edit or replay (only functionalites that are completed)
* Stop the session using the button "Stop Session"

## Possible Reasons the Application is not Working
* The scripts that are in the repo need to become executables. To fix this you can run these commands
```
cd ~/Desktop/CAN-Bus-Visualizer-Sub-System-Prototype/Scripts
chmod +x vcan_s.sh
chmod +x controls_s.sh
chmod +x icsim_s.sh
```
* You didn't clone the repos to their intended locations
* Your password was not entered correctly on step 11
* You didn't download the dependencies