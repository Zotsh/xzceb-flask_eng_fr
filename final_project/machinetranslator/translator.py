import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ['apikey']
api_url = os.environ['url']


if __name__ == "__main__":
    # Prepare the Authenticator
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
    language_translator.set_service_url(api_url)

    # Translate
    translation = language_translator.translate(text=['This is it', 'Something'], model_id='en-fr').get_result()

    # Print results
    print(json.dumps(translation, indent=2, ensure_ascii=False))
