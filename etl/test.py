import requests

url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
params = {"$limit": 200000}  # or 100000 if you’re feeling brave

print("Sending request...")
r = requests.get(url, params=params)
print(f"Status: {r.status_code}")
print(f"Number of records: {len(r.json())}")