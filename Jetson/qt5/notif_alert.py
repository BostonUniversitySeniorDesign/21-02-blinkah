# Get request from server to get text and then play notification on arrow button

import requests
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
    lp_msg1 = (p_tfin[0]['message_text'])
    lp_lp1 = (p_tfin[0]['license_plate'])

    full_msg = (lp_msg1 + "! license plate is: " + lp_lp1)
    print(full_msg)
    return full_msg

    # audio_link = "Audio"
    # audio_param = {'audio': 'audio_link'}
    # a = requests.get(url, params=audio_param)


# if __name__ == "__main__":
#     main()
