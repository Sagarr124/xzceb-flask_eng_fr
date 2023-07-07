import unittest
from ..translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_englishToFrench(self):
        # Test case 1: Translation of 'Hello' to French
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        # Test case 2: Translation of 'Goodbye' to French
        result = english_to_french('Goodbye')
        self.assertEqual(result, 'Au revoir')

    def test_frenchToEnglish(self):
        # Test case 1: Translation of 'Bonjour' to English
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

        # Test case 2: Translation of 'Merci' to English
        result = french_to_english('Merci')
        self.assertEqual(result, 'Thank you')

if __name__ == '__main__':
    unittest.main()