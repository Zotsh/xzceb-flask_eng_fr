import unittest
from .translator import englishToFrench, frenchToEnglish


class TestMethods(unittest.TestCase):

    def testNullEnglishToFrench(self):
        nullEnglish = englishToFrench(None)
        self.assertIsNone(nullEnglish)

    def testNullToFrenchEnglish(self):
        nullFrench = frenchToEnglish(None)
        self.assertIsNone(nullFrench)

    def testHelloEnglishToFrench(self):
        helloToFrench = englishToFrench('Hello')
        self.assertEqual(helloToFrench, 'Bonjour')

    def testBonjourToFrenchEnglish(self):
        bonjourInEnglish = frenchToEnglish("Bonjour")
        self.assertEqual(bonjourInEnglish, 'Hello')
