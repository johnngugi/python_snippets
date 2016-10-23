from caesar_cypher import cypher
import unittest


class TestCase(unittest.TestCase):
    def test_correct_cypher(self):
        self.assertEquals(cypher(3, "abcd"), "defg")

    def test_two(self):
        self.assertEqual(cypher(13, ''), '')

    def test_three(self):
        self.assertEqual(cypher(13, 'Caesar Cipher'), 'Pnrfne Pvcure')
