import unittest

from ListClass import MyList


class TestMyList(unittest.TestCase):
    def test_append(self):
        lst = MyList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(lst.head.data, 1)
        self.assertEqual(lst.head.next.data, 2)
        self.assertEqual(lst.head.next.next.data, 3)
        self.assertIsNone(lst.head.next.next.next)

    def test_duplicate_even(self):
        lst = MyList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        lst.append(4)
        lst.duplicate_even()
        self.assertEqual(lst.head.data, 1)
        self.assertEqual(lst.head.next.data, 2)
        self.assertEqual(lst.head.next.next.data, 3)
        self.assertEqual(lst.head.next.next.next.data, 4)
        self.assertEqual(lst.head.next.next.next.next.data, 2)
        self.assertEqual(lst.head.next.next.next.next.next.data, 4)
        self.assertIsNone(lst.head.next.next.next.next.next.next)

    def test_duplicate_empty_list(self):
        lst = MyList()
        lst.duplicate_even()
        self.assertIsNone(lst.head)


if __name__ == "__main__":
    unittest.main()
