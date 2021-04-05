import requests

REPORTS_ENDPOINT = "http://161.35.50.175:8000/reports/"

files = {'photograph': open('car2.jpg', 'rb')}

# headers = {'Content-type': 'multipart/form-data'}

r = requests.post(REPORTS_ENDPOINT,
    files=files,
    data={
        "license_plate":"test2",
        "speed":54,
        "infraction":"SWERVING",
        "confidence":"0.94",
        "latitude":"47.5",
        "longitude":"63.5",
        "unit_id":42
    }
)

print("HTTP " + str(r.status_code))

print(r.json())