from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lon}"
        else:
            return ("Город ненайден")
    except Exception as e:
        return f"Возникла ошибка: {e}!"


key = '916a0bf01c304190b276f55b2c35b23e'
city = "Москва"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")


