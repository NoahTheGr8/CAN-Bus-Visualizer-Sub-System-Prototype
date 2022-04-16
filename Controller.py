import can
from TrafficDisplayer import TrafficDisplayer
from datetime import datetime
import subprocess

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

    #below is automating commands that analyst need not worry about
    commands = ['ls']
    o = subprocess.run(commands, capture_output=True)
    print(o.stdout)


    #run() starts the GUI and the reading of the packets
    run()
