from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a6e4ec099cae2441a01e579c48941447').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
        print(list_of_data)

    else:
        data = {}

    return render(request,"main/index.html",data)



