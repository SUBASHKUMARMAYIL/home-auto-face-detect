import requests
image_data = open("s1.jpg","rb").read()
response = requests.post("http://localhost:80/v1/vision/face/recognize",
files={"image":image_data},data={"min_confidence":0.40}).json()
for user in response["predictions"]:
   print(user["userid"])
print("Full Response: ",response)