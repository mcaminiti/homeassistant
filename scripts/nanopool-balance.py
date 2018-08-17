import requests
import json

r = requests.get('https://api.nanopool.org/v1/eth/balance/REDACTED')

print r.json()['data']
