import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

packages_str = json.dumps(packages_json[0], indent=2)

print(packages_str)

# https://formulae.brew.sh/api/formula/a2ps.json
