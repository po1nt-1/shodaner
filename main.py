import csv
import inspect
import os
import sys
import time
from pprint import pprint

import shodan

import creepy


class error(Exception):
    pass


SHODAN_API_KEY = creepy.read_token()  # input()
# creepy.write_token(SHODAN_API_KEY)

api = shodan.Shodan(SHODAN_API_KEY)


def _get_script_dir(follow_symlinks=True) -> str:
    '''получить директорию со скриптом'''

    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(_get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def csv_writer(data, name='default.csv'):
    path = os.path.join(_get_script_dir(), name)
    with open(path, 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_reader(name='default.csv'):
    path = os.path.join(_get_script_dir(), name)
    result = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)

    return result


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
    response = api.host(ip)

    request_time = "%.4f" % (time.time() - start)

    results = []
    for i in range(len(response['data'])):
        result = {
            'request_time': str(request_time),
            'ip': str(response.get('ip_str')),
            'country_name': str(response.get('country_name')),
            'hostnames': str(response.get('hostnames')),
            'product': str(response['data'][i].get('product')),
            'os': str(response['data'][i].get('os')),
            'timestamp': str(response['data'][i].get('timestamp')),
            'banner': str(response['data'][i].get('banner')),
            'port': str(response['data'][i].get('port')),
            'org': str(response['data'][i].get('org'))
        }

        results.append(result)

    return results


# print(shodan_info())
# 62.76.6.38   # 142.93.33.2   # 31.31.198.185
res = shodan_host('62.76.6.38')

csv_writer(res)
pprint(csv_reader())
