import requests
import asyncio

from cloudbot import hook


def getbutts():
    request = requests.get("http://api.obutts.ru/noise/1")
    data = request.json()
    url = 'http://media.obutts.ru/noise/{}.jpg'.format(str(data[0]['id']).zfill(5))
    test = requests.get(url)    
    if test.status_code == 200:
        return url
    else:
        return False

@hook.command('tylki', 'tyłki', 'butts')
def obutts(action):
    retry_count = 3
    while retry_count > 0:
        butt = getbutts()
        if butt:
            action('found butt: {}'.format(butt))
            return
        retry_count -= 1
    action('found no butt for you')

