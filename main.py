from opencage.geocoder import OpenCageGeocode
from tkinter import *


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


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")

key = '916a0bf01c304190b276f55b2c35b23e'

window = Tk()
window.title("Координаты городов")
window.geometry("200x100")

entry = Entry()
entry.pack()

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Ввведите город и нажмите на кнопку!")
label.pack()

window.mainloop()
