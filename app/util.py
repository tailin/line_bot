import logging

import requests


def get_short_url(target_url):
    test_access_token = '20f07f91f3303b2f66ab6f61698d977d69b83d64'
    api_url = 'https://api.pics.ee/v1/links/?access_token={}'.format(test_access_token)
    r = requests.post(api_url, data={"url": target_url})
    if r.status_code == 200:
        return r.json()['data']['picseeUrl']
    else:
        logging.error(r.status_code)


def get_exchange_rate():
    r = requests.get('https://tw.rter.info/capi.php')
    mapping = r.json()
    return mapping


def get_reservoir_stat():
    r = requests.get('https://www.taiwanstat.com/waters/latest')
    return r.json()[0]