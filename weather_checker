import requests

data = {
    "Bangalore": {"latitude": 12.9716, "longitude": 77.5946, "current_weather": True},
    "Mumbai":    {"latitude": 19.0760, "longitude": 72.8777, "current_weather": True},
    "Delhi":     {"latitude": 28.6139, "longitude": 77.2090, "current_weather": True}
}

for city, coordinates in data.items():
    r = requests.get("https://api.open-meteo.com/v1/forecast", params=coordinates)
  

    if r.status_code == 200:
        i = r.json()
        temp=i['current_weather']['temperature']
        print(f"Weather data for {city}: {temp}°C, {i['current_weather']['windspeed']} km/h wind speed")
        if temp < 20:
                print(f"Weather in {city} is cold.")
        elif temp < 30:
            print(f"Weather in {city} is moderate.")
        else:
            print(f"Weather in {city} is hot.")
    else:
        print(f"Failed to retrieve weather data for {city}. Status code: {r.status_code}")