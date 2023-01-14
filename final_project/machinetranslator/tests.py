import unittest
from .translator import english_to_french, french_to_english


class TestMethods(unittest.TestCase):

    def testNullEnglishToFrench(self):
        nullEnglish = english_to_french(None)
        self.assertIsNone(nullEnglish)

    def testNullToFrenchEnglish(self):
        nullFrench = french_to_english(None)
        self.assertIsNone(nullFrench)

    def testHelloEnglishToFrench(self):
        helloToFrench = english_to_french('Hello')
        self.assertEqual(helloToFrench, 'Bonjour')

    def testBonjourToFrenchEnglish(self):
        bonjourInEnglish = french_to_english("Bonjour")
        self.assertEqual(bonjourInEnglish, 'Hello')
