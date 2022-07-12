import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        # source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=' +
        #                                 city + '&units=metric&appid=d8d31293bee740761c9ba933823c09ea').read()

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=a49bafb08bc261816ef1c91c532c97db').read()

        
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)                                 


