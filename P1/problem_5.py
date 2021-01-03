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
    return ''.join(random.choice(letters) for oi in range(length))


class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        self.prev = None

    def calc_hash(self):
        sha_key = hashlib.sha256()
        sha_key.update(str(self.data).encode('utf-8'))
        sha_key.update(str(self.timestamp).encode('utf-8'))
        sha_key.update(str(self.previous_hash).encode('utf-8'))
        return sha_key.hexdigest()

    def __str__(self):
        return f"\n[hash = {self.hash}, prev_hash = {self.previous_hash}, data = {self.data}, timestamp = {self.timestamp}]"


class Chain(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def add_chain_link(self, data):
        if self.head is None:
            initial_chain_link = Block(datetime.datetime.utcnow(),
                                       data, "genesis block")
            self.head = initial_chain_link
            self.tail = initial_chain_link
            self.num_elements += 1
            return

        n_chain_block = Block(datetime.datetime.utcnow(), data,
                              self.tail.hash)
        self.tail.next = n_chain_block
        self.tail = n_chain_block
        self.num_elements += 1

    def get_block(self, index):
        if index == 1:
            return self.head
        elif index > 1:
            current = self.head
            i = 0
            while i < index - 1:
                current = current.next
                i += 1
            return current
        return None

    def get_genesis_block(self):
        if self.head is None:
            return None
        return self.head

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
