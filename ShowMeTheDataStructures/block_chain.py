"""
Luis E Gonzalez Hernandez
Block Chain Problem

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
"""
import hashlib
import datetime
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None
        self.prev = None

    def calc_hash(self, data_):
        sha = hashlib.sha256()
        hash_str = data_.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return f"[hash = {self.hash[0:5]}..., prev_hash = {self.previous_hash[0:5]}..., data = {self.data}, timestamp = {self.timestamp}]"


class Chain(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def add_chain_link(self, data):
        if self.head is None:
            initial_chain_link = Block(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"),
                                       data, "INITIAL_CHAIN_HASH")
            self.head = initial_chain_link
            self.tail = initial_chain_link
            self.num_elements += 1
            return

        n_chain_block = Block(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), data,
                              self.tail.hash)
        self.tail.next = n_chain_block
        self.tail = n_chain_block
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() <= 0

    def __str__(self):
        if not self.is_empty():
            current = self.head
            out_string = ""
            while current is not None:
                out_string += str(current) + " -> "
                current = current.next
            out_string = out_string[0:-4]
            return out_string
        return "<EMPTY CHAIN>"


if __name__ == "__main__":
    block_chain = Chain()
    for i in range(5):
        block_chain.add_chain_link(get_random_string(9))
    print(block_chain)
