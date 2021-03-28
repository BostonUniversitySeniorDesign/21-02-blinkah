# full notif .py

# C:\Users\Ram\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts
import sys
import time
import json
import requests
import socket
import playsound
from os.path import join, dirname
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Goal: output an img file, .txt (ALPR), and audio file
# image = image of map
# txt = output message with ALPR
# audio = tts message

# Display on QtPy5 on a new page

# ******1st part*********


def notif_text():
    plates = "ABCD123"

    sample_msg = 'Caution! Dangerous driver ahead. license plate:' + \
        plates + 'Be advised of swerving.'

    return sample_msg


def tts():

    # Compiles warning message with plate reading into .mp3 file
    authenticator = IAMAuthenticator(
        'msSN_rmaBVE-BsIEAb-slPATzinzl2FkBmgHWuXTwqEL')
    service = TextToSpeechV1(authenticator=authenticator)
    service.set_service_url(
        'https://stream.watsonplatform.net/text-to-speech/api')

    text_val = notif_text()

    with open(join(dirname(__file__), './output.mp3'),
              'wb') as audio_file:
        response = service.synthesize(
            text_val, accept='audio/wav',
            voice="en-US_HenryV3Voice").get_result()
        audio_file.write(response.content)


def main():
    tts_op = tts()
    text = notif_text()

    E_P = "http://161.35.50.175:8000/reports/"
    files = {'audio': open('output.mp3', 'rb')}

    r = requests.post(E_P, files=files, data={})

    # print("HTTP " + str(r.status_code))
    with open("output.mp3", "rb") as a_file:
        file_dict = {"output.mp3": a_file}
        response = requests.post(E_P, files)


if __name__ == "__main__":
    main()
