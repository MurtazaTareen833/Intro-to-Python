import requests
response = requests.get("https://www.w3schools.com/")
print(response.text)
# REQUEST MODULE EXAMPLE using GET 
import requests

# Make a GET request
response = requests.get('https://chat.openai.com/')

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()  # Get the response data in JSON format
    print(data)
else:
    # Request failed
    print('Request failed with status code:', response.status_code)

# REQUEST MODULE EXAMPLE USING POST
import requests
import json
url = 'https://chat.openai.com/'
data = {
    'name': 'Murtaza Khan Tareen',
    'email': 'amurtaza293@gmail.com',
    'message': 'Work, Hard!!'
}
json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print('Request failed with status code:', response.status_code)
