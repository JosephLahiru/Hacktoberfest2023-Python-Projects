import random
import time

class Sender:
    def __init__(self):
        self.message = None
        self.seq_num = 0
        self.receiver = None

    def set_receiver(self, receiver):
        self.receiver = receiver

    def send(self):
        if self.seq_num < len(self.message):
            packet = (self.seq_num, self.message[self.seq_num])
            print(f"Sender: Sending packet with SEQ={self.seq_num}: '{packet[1]}'")
            self.receiver.receive(packet)
            self.seq_num += 1

    def set_message(self, message):
        self.message = message

class Receiver:
    def __init__(self):
        self.expected_seq_num = 0

    def receive(self, packet):
        seq_num, data = packet
        if seq_num == self.expected_seq_num:
            print(f"Receiver: Received packet with SEQ={seq_num}: '{data}'")
            self.send_ack(seq_num)
            self.expected_seq_num += 1
        else:
            print(f"Receiver: Discarding out-of-order packet with SEQ={seq_num}: '{data}'")

    def send_ack(self, ack_num):
        time.sleep(1)  
        print(f"Receiver: Sending ACK for SEQ={ack_num}")

def main():
    sender = Sender()
    receiver = Receiver()

    sender.set_receiver(receiver)

    message_to_send = input("Enter the message to send: ")
    sender.set_message(message_to_send)

    while sender.seq_num < len(message_to_send):
        sender.send()

if __name__ == "__main__":
    main()
