#Script to automate different tasks on Webex teams
import requests
import json
import pprint

token = 'NDBiYmZiYzgtY2JkMC00MWU2LWE3NTUtYTE2MDcxMDg3NzYzZDhjYzJlMDctMzI2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

# Create a team

url = 'https://api.ciscospark.com/v1/teams'
headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "name": "Room test"
}

# post_response = requests.post(
#     url, headers= headers, data= json.dumps(body)).json()
# print(post_response)

get_response = requests.get(url, headers= headers).json()

parsed = json.dumps(get_response, indent=2, sort_keys=True)
print (parsed)

