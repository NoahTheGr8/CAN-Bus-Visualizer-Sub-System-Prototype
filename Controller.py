import can
from TrafficDisplayer import TrafficDisplayer
from datetime import datetime

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

def receivePacket():
    msg = bus.recv(timeout=0)
    if msg is not None:
        now = datetime.now()
        date_string = now.strftime('on %B %d at %H:%M:%S')
        print('Message Received %s' %date_string)

    return msg

def run():
    traffic = TrafficDisplayer(1000, receivePacket)

if __name__ == '__main__':
    run()
