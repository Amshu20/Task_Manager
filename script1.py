import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFlODM5NTQ3LWRiNTMtNGZkZS1iY2RlLTY2Njc1ZmY4Y2Q2YiIsImlhdCI6MTc3MzY2MzA3Mywic3ViIjoiZGV2ZWxvcGVyL2RhZDU1ODZhLTJlNWQtNTI0MS05ODY1LTJlNzMyNDE4NWNjMCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjcuNi4xMjIuMjUzIl0sInR5cGUiOiJjbGllbnQifV19.grGXdU8XsM43WHMIaL82Tq-rCugGvdylyaY3QNfsQxkBZVjt_MnD3tv-ODYVdFC7YqTrzy8JJN97R_AgfG-eDg"

tag = "#8UQVUPQV"
tag = tag.replace("#", "%23")

url = f"https://api.brawlstars.com/v1/players/{tag}"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
data = response.json()

print(f"Player: {data['name']}")
print(f"Trophies: {data['trophies']}")
print(f"Total Brawlers: {len(data['brawlers'])}")
print(f"3v3 Wins: {data['3vs3Victories']}")
print(f"Solo Wins: {data['soloVictories']}")
print(f"Club: {data['club']['name']}")

print("\n--- Prestiged Brawlers ---")
brawlers = data['brawlers']
brawlers.sort(key=lambda x: x['trophies'])
print(brawlers[0]['name'])
