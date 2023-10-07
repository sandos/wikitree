import requests

url = 'https://api.wikitree.com/api.php'

params = dict(
    action='getAncestors',
    key='Bäckstrand-5',
    depth="2",
    appId='jb_test_1'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below

for p in data[0]["ancestors"]:
    print(p["Name"], p["Id"], p["Father"], p["Mother"])
