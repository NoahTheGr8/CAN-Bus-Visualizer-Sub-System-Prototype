import can

class PacketManager(object):
    def __init__(self, message: can.Message):
        self.message = message
        self.previous = [message]

    def add(self, message: can.Message):
        self.previous.append(message)

    def get(self):
        return self.previous

    def __str__(self):
        return str(self.message)