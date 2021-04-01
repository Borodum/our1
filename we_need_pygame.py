import pygame
import requests


def HowTheOblast(req):
    title = 'https://geocode-maps.yandex.ru/1.x/'
    geocode = 'geocode=' + req
    apikey = 'apikey=' + '40d1649f-0493-4b70-98ba-98533de7710b'
    format = 'format=' + 'json'
    a = '&'.join([geocode, apikey, format])
    b = '?'.join([title, a])
    result = requests.get(b)
    js = result.json()
    oblast = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    ll = 'll=' + oblast
    spn = 'spn=0.016457,0.00619'
    return oblast


print(HowTheOblast('Австралия'))