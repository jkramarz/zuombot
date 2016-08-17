import requests
from cloudbot import hook

def getBodyPart(part):
    request = requests.get("http://api.o{}.ru/noise/1".format(part))
    data = request.json()
    url = 'http://media.o{}.ru/noise/{}.jpg'.format(part, str(data[0]['id']).zfill(5))
    test = requests.get(url)    
    if test.status_code == 200:
        return url
    else:
        return False

def fetchBodyPart(part):
    retry_count = 3
    while retry_count > 0:
        parts = getBodyPart(part)
        if parts:
            return 'found {}: {}'.format(part, parts)
        retry_count -= 1
    return 'found no {} for you'.format(part)

@hook.command('cycki', 'boobs')
def oboobs(action):
    action(fetchBodyPart('boobs'))

@hook.command('tylki', 'tyłki', 'butts')
def obutts(action):
    action(fetchBodyPart('butts'))
