import requests

REPORTS_ENDPOINT = "http://161.35.50.175:8000/reports/"

def report(imgpath, speed, plate, conf): 
  files = {'photograph': open(imgpath, 'rb')}

  # headers = {'Content-type': 'multipart/form-data'}

  r = requests.post(REPORTS_ENDPOINT,
      files=files,
      data={
          "license_plate":plate,
          "speed": speed,
          "infraction":"SWERVING",
          "confidence":str(conf),
          "latitude":"42.343",
          "longitude":"-71.117",
          "unit_id":00
      }
  )

  print("HTTP " + str(r.status_code))

  print(r.json())