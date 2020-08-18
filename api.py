import json, requests
from datetime import datetime

url = "https://api.github.com/users/zepikeno16/repos"

repositorio = json.loads(requests.get(url).text)

print(repositorio)