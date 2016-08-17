import xmlrpc.client
import requests
import asyncio

from cloudbot import hook

wiki = "https://wiki.hackerspace-krk.pl/"


def do_search(text):
    url = wiki + "lib/exe/xmlrpc.php"
    rpc = xmlrpc.client.ServerProxy(url)
    response  = rpc.dokuwiki.search(text)
    return response

@hook.command('wiki')
def mediawiki(action, text):
    search = do_search(text)
    if(len(search) == 0):
       action('not found')
    else:
        count = 0
        for result in search:
            action('{} - {}{}'.format(result['title'], wiki, result['id']))
            count += 1
            if count == 3:
                action('and {} more'.format(len(search)-3))
                return
    return
