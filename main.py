import time

import shodan

import creepy

SHODAN_API_KEY = creepy.read_token()  # input()
# creepy.write_token(SHODAN_API_KEY)

api = shodan.Shodan(SHODAN_API_KEY)


# def csv_reader(path):
#     with open(path, 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         data = list()
#         for row in reader:
#             data.append(row)
#     return data


# def csv_writer(data, path):
#     try:
#         with open(path, 'a', newline='',) as csv_file:
#             writer = csv.DictWriter(csv_file)
#             if os.path.getsize(new_file_dir) == 0:
#                 writer.writeheader()
#             for row in data:
#                 writer.writerow(row)
#         del data
#         return None
#     except Lil_error as e:
#         raise Lil_error(str(e))


def shodan_info():
    r = api.info()
    result = {
        'plan': r.get('plan'),
        'query_credits': r.get('query_credits'),
        'scan_credits': r.get('scan_credits')
    }

    return result


def shodan_host(ip):
    start = time.time()
    r = api.host(ip)
    request_time = time.time() - start

    data = []
    for i, elem in enumerate(r['data']):
        data.append({})
        data[i].update({'product': elem.get('product')})
        data[i].update({'os': elem.get('os')})
        data[i].update({'banner': elem.get('data')})
        data[i].update({'timestamp': elem.get('timestamp')})
        data[i].update({'port': elem.get('port')})
        data[i].update({'org': elem.get('org')})

    result = {
        'request_time': request_time,
        'ip': r['ip_str'],
        'country_name': r['country_name'],
        'hostnames': r['hostnames'],
        'data': data
    }

    return result
