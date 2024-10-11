import requests

headers = {"Content-Type": "application/json"}
user_input = "What is the capital of Ghana?"

base_url = "https://7663-35-185-179-76.ngrok-free.app"  # Update this with your actual base URL
endpoint = f"{base_url}/generate"
response = requests.post(endpoint, headers=headers, json={
    "inputs": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n",  # Use 'inputs'
    "parameters": {"stop": ["\n", "###"]}  # Use 'parameters' for additional options like 'stop'
})

output = response.json()
print(output)
