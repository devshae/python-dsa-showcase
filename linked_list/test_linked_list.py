# This is a test suite for the LinkedList class defined in linked_list.py.

import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_beginning(self):
        self.linked_list.insert_at_beginning(10)
        self.assertEqual(self.linked_list.head.value, 10)
        self.linked_list.insert_at_beginning(20)
        self.assertEqual(self.linked_list.head.value, 20)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end(30)
        self.assertEqual(self.linked_list.head.value, 30)
        self.linked_list.insert_at_end(40)
        self.assertEqual(self.linked_list.head.next.value, 40)

    def test_delete(self):
        self.linked_list.insert_at_end(50)
        self.linked_list.insert_at_end(60)
        self.linked_list.delete(50)
        self.assertFalse(self.linked_list.search(50))
        self.linked_list.delete(60)
        self.assertFalse(self.linked_list.search(60))

    def test_search(self):
        self.linked_list.insert_at_end(70)
        self.assertTrue(self.linked_list.search(70))
        self.assertFalse(self.linked_list.search(80))

    def test_length(self):
        self.assertEqual(self.linked_list.length(), 0)
        self.linked_list.insert_at_end(90)
        self.assertEqual(self.linked_list.length(), 1)
        self.linked_list.insert_at_end(100)
        self.assertEqual(self.linked_list.length(), 2)

if __name__ == '__main__':
    unittest.main()