import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english


class TestMethods(unittest.TestCase):

    def test_NullEnglishToFrench(self):
        null_english = english_to_french(None)
        self.assertEqual(null_english, "")

    def test_NullToFrenchEnglish(self):
        null_french = french_to_english(None)
        self.assertEqual(null_french, "")

    def test_HelloEnglishToFrench(self):
        hello_to_french = english_to_french('Hello')
        self.assertEqual(hello_to_french, 'Bonjour')

    def test_BonjourToFrenchEnglish(self):
        bonjour_in_english = french_to_english("Bonjour")
        self.assertEqual(bonjour_in_english, 'Hello')
