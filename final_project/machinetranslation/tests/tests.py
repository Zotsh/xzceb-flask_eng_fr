import unittest
<<<<<<<< HEAD:final_project/machinetranslator/tests/tests.py
from final_project.machinetranslator.translator import english_to_french, french_to_english
========
from final_project.machinetranslation.translator import english_to_french, french_to_english
>>>>>>>> b6fb093 (package_folder_structure):final_project/machinetranslation/tests/tests.py


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
