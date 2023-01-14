"""
Translator machine.
"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os import environ
from dotenv import load_dotenv


load_dotenv()
api_key = environ['apikey']
api_url = environ['url']

authenticator = IAMAuthenticator(api_key)

language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(api_url)


def english_to_french(english_text):
    """
    This is to translate English text to French text.
    :param english_text:
    :return:
    """
    if english_text is None:
        return ""
    translation = language_translator.translate(text=[english_text], model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translate some French text to English text.
    :param french_text:
    :return:
    """
    if french_text is None:
        return ""
    translation = language_translator.translate(text=[french_text], model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text


if __name__ == "__main__":
    # Prepare the Authenticator
    print(english_to_french('I am doing just fine'))
    print(french_to_english('Je ne fais que très bien'))
