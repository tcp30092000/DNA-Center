import requests
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = json.dumps({
  "username": "devnetuser",
  "password": "Cisco123!"
})
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)
