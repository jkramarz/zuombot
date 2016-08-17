import requests
import asyncio

from cloudbot import hook


def getboobs():
    request = requests.get("http://api.oboobs.ru/noise/1")
    data = request.json()
    url = 'http://media.oboobs.ru/noise/{}.jpg'.format(str(data[0]['id']).zfill(5))
    test = requests.get(url)    
    if test.status_code == 200:
        return url
    else:
        return False

@hook.command('cycki', 'boobs')
def oboobs(action):
    retry_count = 3
    while retry_count > 0:
        boobs = getboobs()
        if boobs:
            action('found boobs: {}'.format(boobs))
            return
        retry_count -= 1
    action('found no boobs for you')

