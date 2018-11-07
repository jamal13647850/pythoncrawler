import requests

response = requests.get("http://safirmall.com")
response_text = response.text
response_status = response.status_code
print(response_text)
print(response_status)
