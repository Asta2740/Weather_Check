import requests
from datetime import datetime
from plyer import notification

def get_weather_forecast(api_key, lat, lon):
    base_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat},{lon}&days=1&aqi=no&alerts=no'
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        forecast = data['forecast']['forecastday'][0]['hour']
        city = data['location']['name']
        temperature = data['current']['temp_c']
        date = data['forecast']['forecastday'][0]['date']
        return forecast, city, temperature, date
    else:
        return None, None, None, None

def convert_to_12_hour(time):
    return datetime.strptime(time, "%Y-%m-%d %H:%M").strftime("%I %p")

def get_weather_intensity(precipitation):
    if precipitation <= 0.25:
        return 'Light rain'
    elif 0.25 < precipitation <= 4.0:
        return 'Moderate rain'
    elif 4.0 < precipitation <= 16.0:
        return 'Heavy rain'
    elif 16.0 < precipitation <= 50.0:
        return 'Very heavy rain'
    else:
        return 'Extreme rain'

def log_weather_details(city, temperature, date, present_rain_hours, present_no_rain_hours, intensity, precipitation):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('weather_log.txt', 'a') as log_file:
        log_file.write(f" City: {city}, Temperature: {temperature}°C, Current Time: {current_time}, Weather Intensity: {intensity}, Precipitation: {precipitation} mm/hr\n\n")
        log_file.write("\nPresent hours with rain:\n")
        for hour in present_rain_hours:
            log_file.write(hour + '\n')
        log_file.write("\nPresent hours without rain:\n")
        for hour in present_no_rain_hours:
            log_file.write(hour + '\n')
        log_file.write('\n--------------------------------------\n\n')

def check_weather():
    # Replace with your actual API key
    api_key = ''
    # Replace these values with the latitude and longitude of your location
    lat, lon = 31.226763, 29.958498  

    weather_forecast, city, temperature, date = get_weather_forecast(api_key, lat, lon)
    if weather_forecast:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        present_rain_hours = []
        present_no_rain_hours = []
        for hour in weather_forecast:
            weather_desc = hour['condition']['text']
            time_24 = hour['time']
            time_12 = convert_to_12_hour(time_24)
            precipitation = hour['precip_mm']
            intensity = get_weather_intensity(precipitation)

            if time_24 >= current_time:
                if 'rain' in weather_desc.lower():
                    present_rain_hours.append(f"{date} - {time_12} : {weather_desc.capitalize()}, {intensity}, {precipitation} mm/hr")
                else:
                    present_no_rain_hours.append(f"{date} - {time_12} : No rain")

        if present_rain_hours or present_no_rain_hours:
            log_weather_details(city, temperature, date, present_rain_hours, present_no_rain_hours, intensity, precipitation)

            print(f" City: {city}, Temperature: {temperature}°C")
            print(f"Current Time: {current_time}")
            print("Present hours with rain:")
            for hour in present_rain_hours:
                print(hour)
            print("Present hours without rain:")
            for hour in present_no_rain_hours:
                print(hour)

            notification_title = 'Weather Log'
            notification_message = f"City: {city}, Temperature: {temperature}°C\nWeather log details saved."
            notification.notify(
                title=notification_title,
                message=notification_message,
                app_name='Weather App',
                timeout=10
            )

# Run the weather check
check_weather()
