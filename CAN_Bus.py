import can

#Receive message from terminal vcan0

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
msg = can.Message(arbitration_id=0x01, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False)

while True:
    message = bus.recv()
    print(message)

