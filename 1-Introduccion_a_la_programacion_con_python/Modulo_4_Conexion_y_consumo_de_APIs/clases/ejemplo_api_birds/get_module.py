import requests
import json

def requests_get(url):
    return json.loads(requests.get(url).text)


if __name__ == '__main__':
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests_get(url)
    print(len(response))  # 216 aves 