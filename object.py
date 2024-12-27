import requests
image_data = open("pic1.jpg","rb").read()
response = requests.post("http://localhost:80/v1/vision/detection",files={"image":image_data}).json()
for object in response["predictions"]:
    print(object["label"])
    print(response)