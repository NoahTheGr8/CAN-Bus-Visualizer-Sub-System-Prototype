import can

class PacketManager(object):
    def __init__(self, packet: can.Message):
        self.packet = packet