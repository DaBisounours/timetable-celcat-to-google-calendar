""" Downloader Module

This module is used to download content from a given url and eventually save it as a file.

"""
import urllib.request


DEFAULT_URL = 'https://edt.univ-tlse3.fr/FSI/2017_2018/M2/M2_INF_CSA/g251626.xml'


def get_web_page(url=DEFAULT_URL):
    print('Downloading webpage "...'+url[-15:]+'".')
    return urllib.request.urlopen(url)


def save_web_page(name='example.xml', url=DEFAULT_URL):
    response = get_web_page(url)
    print('Saving webpage as ' + name + '.')
    data = response.read()
    with open('downloaded/'+name, 'wb') as output:
        output.write(data)
