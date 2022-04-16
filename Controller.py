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
    p = subprocess.Popen(
            '/home/kali/PycharmProjects/CAN-Bus-Visualizer-Sub-System-Prototype/Scripts/controls_s.sh')
    run()













