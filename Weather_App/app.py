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
            print("Error:", data.get("message"))
            return None
        
        return data

    except Exception as e:
        print("Error fetching weather data:", str(e))
        return None


def display_weather(weather_data):
    if weather_data:
        print("\n===== Current Weather =====")
        print("City:", weather_data['name'])
        print("Country:", weather_data['sys']['country'])
        print("Temperature:", weather_data['main']['temp'], "°C")
        print("Feels Like:", weather_data['main']['feels_like'], "°C")
        print("Min Temp:", weather_data['main']['temp_min'], "°C")
        print("Max Temp:", weather_data['main']['temp_max'], "°C")
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Pressure:", weather_data['main']['pressure'], "hPa")
        print("Wind Speed:", weather_data['wind']['speed'], "m/s")
        print("Condition:", weather_data['weather'][0]['description'].title())
    else:
        print("Weather data not available.")


print("----- Weather Application -----")

api_key = input("Enter your API key: ")

if api_key == "":
    print("API key cannot be empty")
else:
    while True:
        location = input("\nEnter city name or ZIP code: ")

        if location == "":
            print("Location cannot be empty")
            continue

        weather_data = get_weather(api_key, location)

        if weather_data:
            display_weather(weather_data)

        choice = input("\nDo you want to check another city? (yes/no): ").lower()

        if choice != "yes":
            print("Exiting Weather Application")
            break
