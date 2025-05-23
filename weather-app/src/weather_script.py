import requests

API_KEY = '723673b6005d42c3ab4c8fa3e789ada7'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Fetch weather data for a given city."""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.json().get("message"))
        return None

def display_weather(data):
    """Display weather information."""
    if data:
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("No data to display.")

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()