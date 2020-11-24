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


# def csv_reader(path):
#     with open(path, 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         data = list()
#         for row in reader:
#             data.append(row)
#     return data

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
    headers = '|'.join(data.keys())
    vals = '|'.join(data.values())

    with open(path, 'w', encoding="utf-8") as f:
        f.write(headers + '\n' + vals + '\n')


def csv_reader(name='default.csv'):
    path = os.path.join(_get_script_dir(), name)
    with open(path, 'r', encoding='utf-8') as f:
        data = [line[:-1].split('|') for line in f.readlines()]

    return dict(zip(data[0], data[1]))


def fix_slash(string):
    return str(string).replace('\n', '\\n').replace('\r', '\\r')


def shodan_info():
    r = api.info()
    result = {
        'plan': fix_slash(r.get('plan')),
        'query_credits': fix_slash(r.get('query_credits')),
        'scan_credits': fix_slash(r.get('scan_credits'))
    }

    return result


def shodan_host(ip):
    start = time.time()
    r = api.host(ip)
    request_time = time.time() - start

    result = {
        'request_time': fix_slash(request_time),
        'ip': fix_slash(r['ip_str']),
        'country_name': fix_slash(r['country_name']),
        'hostnames': fix_slash(r['hostnames'])
    }

    for i, elem in enumerate(r['data']):
        result.update({f'product_{i}': fix_slash(elem.get('product'))})
        result.update({f'os_{i}': fix_slash(elem.get('os'))})
        result.update({f'banner_{i}': fix_slash(elem.get('data'))})
        result.update({f'timestamp_{i}': fix_slash(elem.get('timestamp'))})
        result.update({f'port_{i}': fix_slash(elem.get('port'))})
        result.update({f'org_{i}': fix_slash(elem.get('org'))})

    return result


res = {'banner_0': 'HTTP/1.1 404 Not Found\\r\\nDate: Sun, 22 Nov 2020 21:12:34 '
       'GMT\\r\\nContent-Type: text/html\\r\\nContent-Length: '
       '536\\r\\nConnection: keep-alive\\r\\n\\r\\n',
       'banner_1': 'HTTP/1.1 404 Not Found\\r\\nDate: Sat, 31 Oct 2020 23:06:40 '
       'GMT\\r\\nContent-Type: text/html\\r\\nContent-Length: '
       '536\\r\\nConnection: keep-alive\\r\\n\\r\\n',
       'country_name': 'Russia',
       'hostnames': '[]',
       'ip': '62.76.6.38',
       'org_0': 'State Educational institution for High professiona',
       'org_1': 'State Educational institution for High professiona',
       'os_0': 'None',
       'os_1': 'None',
       'port_0': '443',
       'port_1': '80',
       'product_0': 'None',
       'product_1': 'None',
       'request_time': '1.001835823059082',
       'timestamp_0': '2020-11-22T21:12:34.884168',
       'timestamp_1': '2020-10-31T23:06:41.029571'}

# res = shodan_host('62.76.6.38')  # 142.93.33.2
# pprint(res)


csv_writer(res)
print(csv_reader())
