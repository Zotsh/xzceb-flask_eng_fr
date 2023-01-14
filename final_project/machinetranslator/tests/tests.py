import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english


class TestMethods(unittest.TestCase):

    def test_NullEnglishToFrench(self):
        nullEnglish = english_to_french(None)
        self.assertIsNone(nullEnglish)

    def test_NullToFrenchEnglish(self):
        nullFrench = french_to_english(None)
        self.assertIsNone(nullFrench)

    def test_HelloEnglishToFrench(self):
        helloToFrench = english_to_french('Hello')
        self.assertEqual(helloToFrench, 'Bonjour')

    def test_BonjourToFrenchEnglish(self):
        bonjourInEnglish = french_to_english("Bonjour")
        self.assertEqual(bonjourInEnglish, 'Hello')
