class Sender:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = [None] * window_size
        self.seq_num = 0
        self.receiver = None

    def set_receiver(self, receiver):
        self.receiver = receiver

    def send(self):
        while self.seq_num < len(self.buffer) and self.seq_num < len(self.buffer):
            packet = self.buffer[self.seq_num]
            print(f"Sender: Sending packet with SEQ={self.seq_num}: '{packet}'")
            self.receiver.receive(packet, self.seq_num)
            self.seq_num += 1

    def receive_ack(self, ack_num):
        print(f"Sender: Received ACK for SEQ={ack_num}")
        self.seq_num = ack_num + 1

    def set_data(self, data):
        self.buffer = list(data)

class Receiver:
    def __init__(self, window_size):
        self.window_size = window_size
        self.expected_seq_num = 0

    def receive(self, packet, seq_num):
        if seq_num == self.expected_seq_num:
            print(f"Receiver: Received packet with SEQ={seq_num}: '{packet}'")
            self.send_ack(seq_num)
            self.expected_seq_num += 1

    def send_ack(self, ack_num):
        print(f"Receiver: Sending ACK for SEQ={ack_num}")

def main():
    window_size = 4
    sender = Sender(window_size)
    receiver = Receiver(window_size)

    sender.set_receiver(receiver)

    data_to_send = input("Enter the data to send: ")
    sender.set_data(data_to_send)

    sender.send()

if __name__ == "__main__":
    main()
