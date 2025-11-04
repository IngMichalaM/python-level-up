# Determine if a given string is a palindrome
# Input: string to evaluate
# Output: Boolean value
# Only consider letters, ignore case and punctuation

import re
import unittest


def identify_palindrome(s: str) -> bool:
    cleaned_text = re.sub(r'[^a-z]', '',  s.lower())
    return cleaned_text == cleaned_text[::-1]


class TestIdentifyPalindrome(unittest.TestCase):
    def test_palindrome_true_czech_no_diacritics(self):
        self.assertTrue(identify_palindrome('Kobyla ma maly bok'))

    def test_palindrome_true_en(self):
        self.assertTrue(identify_palindrome("Go hang a salami - I'm a lasagna hog."))

    def test_palindrome_false(self):
        self.assertFalse(identify_palindrome('This is not a palindrome'))


if __name__ == '__main__':
    unittest.main()
