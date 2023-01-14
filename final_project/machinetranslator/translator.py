import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ['apikey']
api_url = os.environ['url']

authenticator = IAMAuthenticator(api_key)

language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(api_url)


def englishToFrench(englishText):
    translation = language_translator.translate(text=[englishText], model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


if __name__ == "__main__":
    # Prepare the Authenticator
    print(englishToFrench('I am doing just fine'))
