# Get request from server to get text and then play notification on arrow button

import requests
import subprocess
import time
import urllib.request
import json
#import pyaudio


def notif_alert():
    url = "http://161.35.50.175:8000/notifications/"
    lp = "License Plate:"
    nt = "Notification Text:"
    payload = {'license_plate': 'lp', 'message_text': 'nt'}

    # Get request to get JSON data of notification message & license plate
    r = requests.get(url, params=payload)
    # print(r.text)

    p_text = r.text
    p_tfin = json.loads(p_text)
    lp_msg3 = (p_tfin[2]['message_text'])
    lp_lp3 = (p_tfin[2]['license_plate'])
    lp_audio3 = (p_tfin[2]['audio'])

    full_msg = (lp_msg3 + "!\nLicense plate is: " + lp_lp3)
    print(full_msg)

    # urllib.request.urlretrieve(lp_audio3, 'notif.mp3')
    # #r2 = requests.get(lp_audio3, allow_redirects=True)

    # #open('notif.mp3', 'wb').write(r2.content)
    # a = subprocess.Popen(['cvlc', notif.mp3])
    # time.sleep(3)
    # a.kill()
    # # p.play()
    return full_msg

    # audio_link = "Audio"
    # audio_param = {'audio': 'audio_link'}
    # a = requests.get(url, params=audio_param)


# if __name__ == "__main__":
#     out = notif_alert()
