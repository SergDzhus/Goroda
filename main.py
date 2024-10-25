from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return ("Город ненайден")
    except Exception as e:
        return f"Возникла оштбка: {e}!"


key = '916a0bf01c304190b276f55b2c35b23e'
city = "London"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")


