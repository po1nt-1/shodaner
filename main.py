from pprint import pprint

import shodan

import creepy

SHODAN_API_KEY = creepy.read_token()  # input()
# creepy.write_token(SHODAN_API_KEY)

api = shodan.Shodan(SHODAN_API_KEY)


r = api.host('134.209.177.67')

response = {
    'ip': r['ip_str'],
    'country_name': r['country_name'],
    'hostnames': r['hostnames']
}

data = {
    'product': [], 'os': [], 'timestamp': [],
    'port': [], 'org': []
}

for elem in r['data']:
    data['product'].append(elem['product'])

pprint(data)  # pprint(response)
