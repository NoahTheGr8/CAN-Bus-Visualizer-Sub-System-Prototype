import can
from datetime import datetime
import os
import subprocess
from TrafficDisplayer import TrafficDisplayer


bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

def receivePacket():
    msg = bus.recv(timeout=0)
    if msg is not None:
        now = datetime.now()
        date_string = now.strftime('on %B %d at %H:%M:%S')
        print('Message Received %s \n' %date_string, msg)

    return msg

def run():
    traffic = TrafficDisplayer(ms=1, function=receivePacket)

if __name__ == '__main__':
    # below is automating commands that analyst need not worry about

    curr_dir = os.getcwd() #current working dir
    script_dir = curr_dir + '/Scripts' #directory with all the scripts

    #Step 1. Load the virtual CAN module, set up virtual interface, and ensure its up and running - vcan_s.sh
    command1 = './vcan_s.sh'
    p1 = subprocess.run(command1, shell=True, cwd = script_dir , capture_output=False)

    #Step 2. Nav to ICSim folder and start up the vcan0 (speedometer) - includes ./icsim vcan0
    command2 = './icsim_s.sh'
    p2 = subprocess.Popen(command2, shell=True, cwd=script_dir)

    #Step 3. Set up  the CAN Bus Control Panel (xbox controller image) - includes ./controls vcan0
    command3 = './controls_s.sh'
    p3 = subprocess.Popen(command3, shell=True, cwd=script_dir)

    # run() starts the GUI and the reading of the packets
    run()
