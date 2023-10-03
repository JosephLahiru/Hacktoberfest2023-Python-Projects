class Sender:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = [None] * window_size
        self.seq_num = 0
        self.receiver = None

    def set_receiver(self, receiver):
        self.receiver = receiver

    def send(self):
        for i in range(self.window_size):
            if self.seq_num < len(self.buffer):
                packet = self.buffer[self.seq_num]
                print(f"Sender: Sending packet with SEQ={self.seq_num}: '{packet}'")
                self.receiver.receive(packet, self.seq_num)
                self.seq_num += 1

    def receive_ack(self, ack_num):
        print(f"Sender: Received ACK for SEQ={ack_num}")
        for i in range(ack_num + 1):
            if i < len(self.buffer):
                self.buffer[i] = None

    def set_data(self, data):
        self.buffer = list(data)

class Receiver:
    def __init__(self, window_size):
        self.window_size = window_size
        self.expected_seq_num = 0
        self.buffer = [None] * window_size

    def receive(self, packet, seq_num):
        if seq_num >= self.expected_seq_num and seq_num < self.expected_seq_num + self.window_size:
            print(f"Receiver: Received packet with SEQ={seq_num}: '{packet}'")
            self.buffer[seq_num - self.expected_seq_num] = packet
            self.send_ack(seq_num)

    def send_ack(self, ack_num):
        print(f"Receiver: Sending ACK for SEQ={ack_num}")
        self.expected_seq_num = ack_num + 1

    def get_data(self):
        filtered_buffer = filter(lambda x: x is not None, self.buffer)
        return ''.join(filtered_buffer)

def main():
    window_size = 4
    sender = Sender(window_size)
    receiver = Receiver(window_size)

    sender.set_receiver(receiver)

    data_to_send = input("Enter the data to send: ")
    sender.set_data(data_to_send)

    while sender.seq_num < len(data_to_send):
        sender.send()

    received_data = receiver.get_data()
    print("\nReceived Data at Receiver:", received_data)

if __name__ == "__main__":
    main()