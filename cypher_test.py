from caesar_cypher import cypher
import unittest


class testCase(unittest.TestCase):
    def test_correct_cypher(self):
        self.assertEquals(cypher("abcd"), "DEFG")
