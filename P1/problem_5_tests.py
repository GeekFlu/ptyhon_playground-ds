import unittest

from problem_5 import Chain, get_random_string


class BlockChainTests(unittest.TestCase):

    def test_block_chain(self):
        block_chain = Chain()
        for i in range(5):
            block_chain.add_chain_link(get_random_string(9))
        self.assertEqual(5, block_chain.size())

    def test_validate_blocks(self):
        block_chain = Chain()
        block_chain.add_chain_link("bloque 1 - genesis")
        block_chain.add_chain_link("bloque 2 - real data 2")
        block_chain.add_chain_link("bloque 3 - real data 3")
        for i in range(100):
            block_chain.add_chain_link(get_random_string(10))

        b90 = block_chain.get_block(90)
        b91 = block_chain.get_block(91)
        self.assertEqual(b90.hash, b91.previous_hash)

        b10 = block_chain.get_block(10)
        b11 = block_chain.get_block(11)
        self.assertEqual(b10.hash, b11.previous_hash)


if __name__ == "__main__":
    unittest.main()
