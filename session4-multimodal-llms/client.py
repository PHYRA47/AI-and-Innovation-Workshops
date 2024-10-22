import requests
import json

# Update this with your actual Ngrok URL
base_url = "https://ad37-35-231-68-120.ngrok-free.app"

def test_text_generation():
    endpoint = f"{base_url}/generate_text"
    headers = {"Content-Type": "application/json"}
    payload = {
        "inputs": "What is the capital of Syria?"
    }
    
    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print("Text Generation Result:")
        print(json.dumps(result, indent=2))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def test_image_text_generation():
    endpoint = f"{base_url}/generate_text_image"
    
    # Replace 'path_to_your_image.jpg' with the actual path to your image file
    files = {'file': open('image1.jpg', 'rb')}
    data = {'prompt': 'Describe this image', 'language': 'en'}
    
    response = requests.post(endpoint, files=files, data=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Image-Text Generation Result:")
        print(json.dumps(result, ensure_ascii=False, indent=2)) # ensure_ascii=False to get non-ASCII characters properly formatted
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("Testing Text Generation:")
    test_text_generation()
    
    print("\nTesting Image-Text Generation:")
    test_image_text_generation()

"""
import requests
from PIL import Image

headers = {"Content-Type": "application/json"}

# Load the image and convert it to RGB
image_path = "image1.jpg"
image = Image.open(image_path).convert('RGB')

# Define the prompt or question
question = "Identify the car in the image"

# Define the base URL and the endpoint
base_url = "https://768f-34-16-160-180.ngrok-free.app"  # Replace with the actual base URL
endpoint = f"{base_url}/generate"

# Prepare the request payload
payload = {
    "inputs": f"Image: image1.jpg\nQuestion: {question}",  # inputs field with image path and question
    "parameters": {"stop": ["\n", "###"]}  # parameters field if needed
}

# Send the POST request with the image and question
response = requests.post(endpoint, headers=headers, json=payload)

# Get the output from the response
output = response.json()
print(output)
"""