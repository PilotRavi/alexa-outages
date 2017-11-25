import requests, json
from datetime import datetime

url = 'http://outagemap.dominionenergy.com.s3.amazonaws.com/resources/data/external/interval_generation_data/2017_11_25_09_00_30/report_region.json'

def return_json(URL):
    response = requests.get(URL)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

    return response

json_str = return_json(url).text

if json_str[:5] != "Error":
    parsed = json.loads(json_str)
    print(parsed['file_data']['areas'][0]['cust_a']['val'])
utc = datetime.utcnow().strftime("%Y_%m_%d_%H_%M_30")
print (utc)
