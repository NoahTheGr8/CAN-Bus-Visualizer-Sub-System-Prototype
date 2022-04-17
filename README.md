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
* "kali" is your password for your kali linux (scripts won't work if it's not "kali")
* You follow these instructions **EXACTLY** as they are (scripts won't work since they depend on certain directory calls)

## How to Get Started
5. Open Kali Linux
6. Open a terminal/command prompt
7. Download the dependencies
```
sudo apt install can-utils
sudo apt install libsdl2-dev libsdl2-image-dev -y
```
6. Navigate to the desktop
```
cd ~/Desktop
```
8. Clone this repository to the **Desktop**
```
git clone https://github.com/NoahTheGr8/CAN-Bus-Visualizer-Sub-System-Prototype.git
```
8. Create another folder called "w_can" on the **Desktop**
```
mkdir w_can
```
9. Navigate into the folder w_can 
```
cd ~/Desktop/w_can
```
10. Clone the simulator repository into the folder **w_can**
```
git clone https://github.com/zombieCraig/ICSim.git
```
11. Navigate to folder where the CAN Bus Visualizer System is
```
cd ../CAN-Bus-Visualizer-Sub-System-Prototype
```
12. Start the program using the below command - 
```
python3 Controller.py
```
13. Enjoy (hopefully) :)

## How to use the prototype
* look at it and see all packets being sent on the CAN Bus
* Right click a packet (represented as a row) and choose to edit or replay (only functionalites that are completed)
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
* Your password is not "kali"
* You didn't download the dependencies

