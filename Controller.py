import can
from TrafficDisplayer import TrafficDisplayer

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)


def receivePacket():
    msg = bus.recv(timeout=100)
    if msg is not None:
        print('Message Received')

    return msg


def run():
    traffic = TrafficDisplayer(1000, receivePacket)


if __name__ == '__main__':
    run()
