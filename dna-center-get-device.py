import requests
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/network/device"

payload = json.dumps({
  "username": "devnetuser",
  "password": "Cisco123!"
})
headers = {
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY3NzQ3NTA3NCwiaWF0IjoxNjc3NDcxNDc0LCJqdGkiOiI3ZDJhYzgxZC1lYjAzLTRjOGItYjliOS02Y2YwZjlkYjA1ODAiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.FskY6fNZyLI-jRVZQFHfmvQeSFJ6kD5aforR0w9mAKJi2WLdEgxvFtlV-7qXE7o1TPvVZc_ISj_2gwBfrid4ggARcc_55uS8ATM26W0U3_dRJQBONUr0IH2iiMnkuKcPVyqZwiOnjWqfQfl_uEekQR07xpRisOC20sRcws2hvdMsiT9siXNxNeoG6ZtpSct5UOteU33tPCSqeHo8-NX21TXwR6dMoWCq1BDw1erzXlVzwNxkPl8ousjPDxIJyKGixzx7zqiv_HLFH50YdQBvMILBuzbbGDHij5RtAT6HzEPJPApYN3x-gC5b8Ljcdn30TuM2qYUewyW1b6juSYwzCw',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)
