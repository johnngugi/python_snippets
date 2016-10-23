from linked_list import LinkedList

import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def test_insert(self):
        self.list.insert("David")

        self.assertTrue(self.list.head.get_data() == "David")
        self.assertTrue(self.list.head.get_next() is None)

if __name__ == '__main__':
	unittest.main()
