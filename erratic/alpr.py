# alpr -c us (name_of_img) 
# Save output as JSON

import json
import os
import requests
import subprocess
import sys

# images are saved locally but can be accessed from website using wget
#print("Enter a value from 1 to 26")
def alpr(path):

  # Making CLI call to generate plate readings
  #os.system("alpr -c us " + pic_val)
  proc = subprocess.Popen(["alpr -c us "+path], stdout = subprocess.PIPE, shell = True)
  (out, err) = proc.communicate()

  use_val = str(out, 'utf-8')

  hyphen = use_val.find('-')
  use_val = use_val[hyphen+2:]



  # Removes hyphen from output
  p_val = use_val.split('- ')
  #print (p_val)

  # Initializing array of dicts
  plates = []

  # Parsing through string output generated from alpr command to format data 
  # Get rid of unnecessary spaces, characters, tabs, new lines, etc
  for elem in p_val:
    
    key = elem.find('\t')
    #print (elem[0:key])

    key2 = elem.find(':')
    #print (elem[key2+2:])
    
    key3 = elem.find('\n')

    plate =  elem[0:key]
    conf = elem[key2+2:key3]

    if (plate == ''):
      plate = 'NOIMG'
      conf = '0'
    if (plate == 'o license plates found.' or conf == ' license plates found.'):
      plate = ''
      conf = '0'
    


    plates.append({'license_plate': plate, 'confidence': float(conf)})

  #print (plates)

  # Store plates (dict) as JSON in Reports.json

  return plates

# ******************2nd part******************
# Need to send generated data to server
# Specifically post request to /reports/

# url = 'http://161.35.50.175:8000/reports'
# files = {'media': open('Reports.json', 'rb')}
# requests.post(url, files=files)
