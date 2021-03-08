# coding=utf-8
import json
from os.path import join, dirname
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def main():
    authenticator = IAMAuthenticator(
        'msSN_rmaBVE-BsIEAb-slPATzinzl2FkBmgHWuXTwqEL')
    service = TextToSpeechV1(authenticator=authenticator)
    service.set_service_url(
        'https://stream.watsonplatform.net/text-to-speech/api')

    #voices = service.list_voices().get_result()
    #print(json.dumps(voices, indent=2))
    text = 'Introducing Blinkah: Revolutionizing the Road.'
    sample_msg = 'Warning! Caution! Dangerous driver ahead. license plate: 4. A. L. P. R. 6. Q. W.'

    with open(join(dirname(__file__), './output.wav'),
              'wb') as audio_file:
        response = service.synthesize(
            sample_msg, accept='audio/wav',
            voice="en-US_HenryV3Voice").get_result()
        audio_file.write(response.content)


if __name__ == "__main__":
    main()
