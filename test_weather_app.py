import requests
import secret_key


API_KEY = secret_key.API_KEY

def test_get_weather_data():
    city = "New York"
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&days=1"
    response = requests.get(url).json()

    weather_data = {
        'city': response['location']['name'],
        'temperature': response['current']['temp_f'],
        'description': response['current']['condition']['text'],
        'icon': response['current']['condition']['icon']
    }

    print("\n")
    print(f"City: {weather_data['city']}")
    print(f"Temperature: {weather_data['temperature']}")
    print(weather_data['description'])