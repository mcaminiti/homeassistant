import requests
import json

r = requests.get('https://api.nanopool.org/v1/eth/hashrate/REDACTED')

print r.json()['data']
