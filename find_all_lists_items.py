import unittest
from typing import List


def index_all(lst: List, lookfor_string) -> List:
    """ Find all items in the list and sublist and return a list of indexes. """
    index_list = []
    for index, item in enumerate(lst):
        if isinstance(item, list):
            sub_list = index_all(item, lookfor_string)
            for i in sub_list:
                index_list.append([index] + i)
        else:
            if item == lookfor_string:
                index_list.append([index])
    return index_list


class TestSortString(unittest.TestCase):
    def test_find_index_basic_list(self):
        self.assertEqual([[0], [4]], index_all([5, 8, 9, 6, 5], 5))

    def test_find_index_one_sublist(self):
        self.assertEqual([[0], [1, 2], [4]], index_all([5, [0, 4, 5], 9, 6, 5], 5))

    def test_find_index_complex_list(self):
        self.assertEqual([[0, 0, 1], [0, 1], [1, 1]], index_all([[[1, 2, 3], 2, [1,3]], [1, 2, 3]], 2))


if __name__ == '__main__':
    unittest.main()
