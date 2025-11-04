#  Write a function to sort the words in a string
#  Input: string of words, separated by spaces
#  Output: string with the words sorted alphabetically
#  Ignore case, but keep the case

import unittest


def sort_string(s: str) -> str:
    words = s.split()
    words.sort(key=str.lower)
    return ' '.join(words)


class TestSortString(unittest.TestCase):
    def test_sort_string_lower_case(self):
        self.assertEqual("apple banana cherry", sort_string("banana cherry apple"))

    def test_sort_string_upper_case(self):
        self.assertEqual("Apple Banana Cherry Melon", sort_string("Banana Melon Cherry Apple"))

    def test_sort_string_mix_case(self):
        self.assertEqual("Apple banana cherry MEDOW melon miaow", sort_string("MEDOW banana melon cherry Apple miaow"))


if __name__ == '__main__':
    unittest.main()
