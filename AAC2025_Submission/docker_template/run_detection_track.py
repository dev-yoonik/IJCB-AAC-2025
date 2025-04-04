import os
import json
import requests

# Detection endpoint
url = "http://0.0.0.0:7007/detection/detect"

# Get the name where the images are and where to save results
images_dir = os.environ.get("images_dir")
save_dir = os.environ.get("save_dir")

# Load detection protocol
protocol = os.path.join(images_dir, "detection_track.txt")
responses = []

# Send requests
with open(protocol, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        params = {
            "image_path": os.path.join(images_dir, line)
        }
        response = requests.get(url, params=params)
        print(response.json())
        responses.append(response.json())

# Save responses
with open(os.path.join(save_dir, "detection_track.json"), "w") as f:
    json.dump(responses, f, indent=4)