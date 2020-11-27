import csv
import inspect
import os
import sys
import time
from pprint import pprint

import shodan

import creepy


class Local_error(Exception):
    pass


api = shodan.Shodan('')


def start(token=''):
    global api

    if token:
        creepy.write_token(token)
    token = creepy.read_token()
    api = shodan.Shodan(token)


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


def gen_new_csv_name():
    path = os.path.join(_get_script_dir(), 'results')
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(path)
    i = 1
    while f"result{i}.csv" in files:
        i += 1

    return os.path.join(path, f"result{i}.csv")


def csv_writer(data, path):
    if not os.path.exists(os.path.join(_get_script_dir(), 'results')):
        os.mkdir(os.path.join(_get_script_dir(), 'results'))

    with open(path, 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_reader(path):
    if not os.path.exists(os.path.join(_get_script_dir(), 'results')):
        os.mkdir(os.path.join(_get_script_dir(), 'results'))

    result = []
    with open(path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def shodan_info():
    global api

    r = api.info()
    result = {
        'plan': str(r.get('plan')),
        'query_credits': str(r.get('query_credits')),
        'scan_credits': str(r.get('scan_credits'))
    }

    return result


def shodan_host(ip):
    global api

    start = time.time()
    try:
        response = api.host(ip)
    except shodan.exception.APIError as e:
        raise Local_error(str(e))

    time_spent = "%.4f" % (time.time() - start)

    results = []
    for i in range(len(response['data'])):
        result = {
            'time_spent': str(time_spent),
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
