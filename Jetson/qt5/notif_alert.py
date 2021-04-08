# Get request from server to get text and then play notification on arrow button

import requests
import subprocess
import time
import urllib.request
import json


def notif_alert():
    url = "http://161.35.50.175:8000/notifications/"
    lp = "License Plate:"
    nt = "Notification Text:"
    payload = {'license_plate ': 'lp', 'message_text': 'nt'}

    # Get request to get JSON data of notification message & license plate
    r = requests.get(url, params=payload)
    p_text = r.text
    p_tfin = json.loads(p_text)
    lp_msg3 = (p_tfin[4]['message_text'])
    lp_lp3 = (p_tfin[4]['license_plate'])
    lp_audio3 = (p_tfin[4]['audio'])

    full_msg = (lp_msg3 + "!\nLicense plate is: " + lp_lp3)
    print(full_msg)

    # urllib.request.urlretrieve(lp_audio3, 'notif.mp3')
    # # r2 = requests.get(lp_audio3, allow_redirects=True)
    # # open('notif2.mp3', 'wb').write(r2.content)
    # a = subprocess.Popen(['cvlc', 'notif.mp3'])
    # time.sleep(3)
    # a.kill()
    return full_msg


if __name__ == "__main__":
    out = notif_alert()
