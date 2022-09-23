import requests
from settings import API_KEY, BASE_URL


class Weather:
    complete_url = BASE_URL + "appid=" + API_KEY + "&q="
    @classmethod
    def get_temp(self, city):
        response = requests.get(self.complete_url + city).json()
        temp_info = {
            'temperature now:': response['main']['temp'],
            'feels like:': response['main']['feels_like'],
            'max:': response['main']['temp_max'],
            'min:': response['main']['temp_min']

        }
        for i in temp_info.keys():
            temp_info[i] = Weather.__kelvin_to_celcius(temp_info[i])
        return temp_info

    def __kelvin_to_celcius(kelvin):
        return round(kelvin - 273.15, 1)

