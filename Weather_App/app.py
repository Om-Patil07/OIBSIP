import requests

def get_weather(api_key, location):
    url = "http://api.openweathermap.org/data/2.5/weather"
    
    if location.isdigit():
        params = {'zip': f"{location},in", 'appid': api_key, 'units': 'metric'}
    else:
        params = {'q': location, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print(f"Error: {data.get('message')}")
            return None
        
        return data

    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")
        return None


def display_weather(weather_data):
    if weather_data:
        print("\n===== Current Weather =====")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Condition: {weather_data['weather'][0]['description'].title()}")
    else:
        print("Weather data not available.")


if __name__ == "__main__":
    api_key = input("Enter your API key: ")
    location = input("Enter city name or ZIP code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)
