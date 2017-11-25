import requests, json

url = 'http://outagemap.dominionenergy.com.s3.amazonaws.com/resources/data/external/interval_generation_data/2017_11_25_07_15_30/report_region.json'
response = requests.get(url)

parsed = json.loads(response.text)
print(parsed['file_data']['areas'][0]['cust_a']['val'])
