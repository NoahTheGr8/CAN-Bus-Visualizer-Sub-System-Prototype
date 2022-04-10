import can

file = open("data.txt", 'w')


#socketcan allow us to run read can-utils messages
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=30000)
msg = can.Message(arbitration_id=0x01, data=[0,25, 0, 1, 3, 1, 4, 1], is_extended_id=False)

#bus.send(msg)

for i in range(25):
    message = bus.recv()
    temp = str(message)
    temp2 = temp.split()
    time_stamp_var = temp2[1]
    canv0 = temp2[-1]
    info = temp2[3]
    returned_text = time_stamp_var + " " + canv0 + " " + info
    print(returned_text)
    file.write(returned_text)
    file.write('\n')

file.close()
