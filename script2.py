import requests
token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjYTQ3YzQ3LTA0ZDEtNGVhNC04ODk0LWNjODQyMjMyZGFhNSIsImlhdCI6MTc3MzY2NDE1MCwic3ViIjoiZGV2ZWxvcGVyLzBlOGI0MjRmLWY2MjEtMzY1MC01NThiLTFmNzEyN2FhMGQ4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjI3LjYuMTIyLjI1MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.X2hgmGO1tT9-uqMHB6xgOHa9iP-U9yNpEc_ISET1p-tj5XOAmctEAQf4Q9X27M_cfE5sKPMRrfjNYVt-x0h2OQ"
tag="#QPCQ99JQL"
tag=tag.replace("#","%23")
url=f"https://api.clashofclans.com/v1/players/{tag}"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
data = response.json()
'''print(f"Player: {data['name']}")
print(f"Troops: {data['troops']}")
#print(f"Town Hall: {data['townhall']}")
print(f"Heroes: {data['heroes']}")
print(f"Spells: {data['spells']}")
#print(f"Siege Machines: {data['siegemachines']}")
#print(f"Guardians: {data['guardians']}")
#print(f"Pets: {data['pets']}")
#print(f"Gold: {data['gold']}")'''
a=0
name=""
for i in data['troops']:
    if i['village']=='home':
        if a<(i['maxLevel']-i['level']):
            a=(i['maxLevel']-i['level'])
            name=i['name']
print(a,name)
