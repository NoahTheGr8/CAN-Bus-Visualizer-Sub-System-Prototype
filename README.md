# CAN-Bus-Visualizer-Sub-System-Prototype
This repository contains a technical prototype for a sub-system within the CAN-Bus Visualizer System.

## About this program's functionality
This project's main purpose is to view the CAN Bus traffic in real time, replay packets, and edit packets of interest by the analyst.

## Status of the implementation
We implemented various functionalities based on the requeriments of the customer.

* Implemented a GUI to vizualize the packets.
* Implemented functionalities for edit and replay packets.
* Implemented the use of scripts to automate processes that start the virtual CAN and simulator.

## Missing functionalities
* Decoding of the packets
* Allowing the Analyst to Manage Project
* Allowing the Analyst to Manage CAN Traffic except displaying traffic, editing packets and replaying packets
* Allowing the Analyst to Manage a CAN Map


## What we learned
We learned various things after taking on this prototype project. We learned -
* How to communicate when collaborating on a coding project
* How to use git-hub
* How to use git
* How to use the documentation we made previously to help us in achieving the requirements

Also, we asked ourselves some important questions that we had not considered until we started working on the code such as "What happens after editing a packet?" or "What should the UI present about a packet?". Although we had documentations on most of the scenarios, it was only in the coding portion that we could consider new things. 

Overall, the most important things we learned was using the git and git-hub software to meet the technical prototype requirements as well as new perspectives to consider for the final implementation. 

## Prerequisites/Assumptions to using this program
* Kali Linux 
* Python 3.9+
* You follow these instructions **EXACTLY** as they are (scripts won't work since they depend on certain directory calls)

## How to start application
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

## How to use the program 
* Look at it and see all packets being sent on the CAN Bus
* Right-click a packet (represented as a row) and choose to edit, view previous versions of a packet, or replay (only functionalites that are completed)
* Stop the session using the button "Stop Session to close program and all the UI's it created"

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
