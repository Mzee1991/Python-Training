import json
import requests

r = requests.get('https://www.yahoofinanceapi.com/yh-finance-api-specification.json')
api_specification_json = r.json()

specification_str = json.dumps(api_specification_json, indent=2)

with open('yahoo_api.json', 'w') as f:
    f.write(specification_str)
