import os
import requests
image_folder = "test_img3"
files = {}
for i, filename in enumerate(os.listdir(image_folder)):
    if filename.endswith(".jpg"):
        with open(os.path.join(image_folder, filename), "rb") as f:
            files[f"image{i+1}"] = f.read()
response = requests.post("http://localhost:80/v1/vision/face/register",
                         files=files,
                         data={"userid": "Unknown"}).json()
print(response)