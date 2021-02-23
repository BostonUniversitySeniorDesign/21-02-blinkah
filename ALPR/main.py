# Python script to run OpenALPR code & create post requests

# ******************1st part******************
# alpr -c us (name_of_img) 
# Save output as JSON

# main.py
import json
import os
import requests
import subprocess
import sys

# images are saved locally but can be accessed from website using wget
print("Enter a value from 1 to 26")
car_num = input()

# parsing user input & concatenating it
pic_val = "car"+car_num+".jpg"

# Making CLI call to generate plate readings
#os.system("alpr -c us " + pic_val)
proc = subprocess.Popen(["alpr -c us "+pic_val], stdout = subprocess.PIPE, shell = True)
(out, err) = proc.communicate()

use_val = str(out, 'utf-8')

hyphen = use_val.find('-')
use_val = use_val[hyphen+2:]

# Removes hyphen from output
asdf = use_val.split('- ')
#print (asdf)

# Initializing array of dicts
plates = []

# Parsing through string output generated from alpr command to format data 
# Get rid of unnecessary spaces, characters, tabs, new lines, etc
for elem in asdf:
    
    key = elem.find('\t')
    #print (elem[0:key])

    key2 = elem.find(':')
    #print (elem[key2+2:])
    
    key3 = elem.find('\n')

    plates.append({'license_plate': elem[0:key], 'confidence': float(elem[key2+2:key3])})

print (plates)

# Store plates (dict) as JSON in Reports.json
with open("Reports.json", "w") as outfile:
    json.dump(plates, outfile)

# ******************2nd part******************
# Need to send generated data to server
# Specifically post request to /reports/

url = '161.35.50.175:8000/reports/'
files = {'media': open('Reports.json', 'rb')}
requests.post(url, files=files)
files2 = {'media': open('car1.jpg', 'rb')}
requests.post(url, files=files2)
