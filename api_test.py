import requests
from datetime import datetime as dt

url = 'https://api.wikitree.com/api.php'

params = dict(
    action='getAncestors',
    key='Bäckstrand-5',
    depth="1",
    appId='jb_test_1'
)

now = dt.now()
resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below
print(f"Took {dt.now()-now}")

print(data)

num = 0

for p in data[0]["ancestors"]:
    print(p["Name"], p["Id"], p["Father"], p["Mother"])
    num += 1


print(data[0]["ancestors"][0])
print(f"Number {num}")
