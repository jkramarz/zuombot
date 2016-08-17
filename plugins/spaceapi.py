import requests
import asyncio

from cloudbot import hook

spaceapi = "http://hskrk-spacemon.herokuapp.com"
def check_anyone():
    request = requests.get(spaceapi)
    if request.status_code == 200:
        data = request.json()
        return data
    else:
        return False

@hook.command('anyone', 'at')
def anyone(action):
    check = check_anyone()
    print(check)
    if check != False:
        if check['state']['open'] == True:
            action('HSKRK is open! 😂')
        else:
            action('HSKRK is now closed. 😞')
    else:
        action('cannot connect to spaceapi')
    return
