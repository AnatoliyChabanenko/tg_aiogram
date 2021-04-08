import googlemaps


me = ('46.955949', '31.995631')
point = ('50.483879', '30.481361')
API_KEY = 'AIzaSyD0LQ8x79xZMXdv85GjBitzYiAr814bNXU'
gmaps_client = googlemaps.Client(key=API_KEY)

d = gmaps_client.distance_matrix(
    origins=me,
    destinations=(point[0], point[1]),
    mode='driving',
)

if __name__ == '__main__':
    print(d)
    a = d['rows'][0]['elements'][0]['distance']['text']
    print(a)