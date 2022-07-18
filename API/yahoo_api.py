import requests
import json

url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-api-key': "YBNU1Xkxhl8NJePwg3Bv08i0Mdom0iT5ahHpUDbn"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

j_response = response.json()
jstr_response = json.dumps(j_response, indent=2)

print(jstr_response)

#print(response.text)
