import requests

from cloudbot import hook

@hook.regex('https?:\/\/(?P<url>(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*))')
def textance(match, action):
    query = 'http://textance.herokuapp.com/title/{}'.format(match.group('url'))
    title = requests.get(query)
    if title.status_code == 200:
        return title.text
