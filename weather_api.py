import json
from secrets import WEATHER_API_KEY

import requests


def get_temp_api(city_id, units):
    params = {"appid": WEATHER_API_KEY, "id": id, "units": units}
    url = "http://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url, params=params)
    data = json.loads(r.text)
    if data["cod"] == 200:
        return {"temperature": data["main"]["temp"]}
    else:
        return {"temperature": data["message"]}

    # print(data.keys())


if __name__ == "__main__":
    id = "2648579"
    units = "metric"
    WEATHER_API_KEY += "1324123"
    data = get_temp_api(id, units)
    print(data)
