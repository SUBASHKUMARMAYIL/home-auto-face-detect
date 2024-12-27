import requests
response = requests.post("http://localhost:80/v1/vision/face/delete",
data={"userid":"Unknown"}).json()
print(response)