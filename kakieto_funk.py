import json

import googlemaps
from geopy.distance import geodesic
from config2 import API_KEY , NIKO


def praice(name: str):
    data = json.load(open('data1.json'))
    return data[name]


class Coord:
    lat: float = 0.0
    lon: float = 0.0

class GetDistatnse:

    @classmethod
    def calc(cls, c1: Coord, c2: Coord):
        raise NotImplementedError


class Simplecalc(GetDistatnse):

    @classmethod
    def calc(cls, c1: Coord, c2: Coord):
        return geodesic((c1.lat, c1.lon), (c2.lat, c2.lon)).km


def roztoyanie(location: dict):

    you = (location['latitude'], location['longitude'])
    km = geodesic(NIKO, you).km
    return int(km)

def proschet(location: dict):
    you = (location['latitude'], location['longitude'])
    gmaps_client = googlemaps.Client(key=API_KEY)

    d = gmaps_client.distance_matrix(
        origins=NIKO,
        destinations=(you),
        mode='driving',
    )
    return d['rows'][0]['elements'][0]['distance']['text'].replace('km', '')


if __name__ == '__main__':
    pass
# пару розчетев  клас метод делать наследника потом розщети по другому
# парсер в класс
