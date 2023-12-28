# Weather Checking App

This Python script retrieves weather forecasts using the WeatherAPI. It fetches weather details based on specified latitude and longitude coordinates, logs the information into a file, and provides real-time notifications.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Features

- **Weather Forecast:** Retrieves weather details for the specified location.
- **Logging:** Stores weather details in a log file for future reference.
- **Notifications:** Provides real-time notifications about the current weather.

## Setup

1. **API Key:** Obtain an API key from WeatherAPI. Replace the placeholder in the script (`api_key = ''`) with your actual API key.
2. **Coordinates:** Set the latitude and longitude coordinates for your desired location (`lat, lon = <your_latitude>, <your_longitude>`).

## Usage

Run the Python script to check the current weather conditions and receive notifications.

bash
python weather_app.py

## Dependencies
This script requires the following Python packages:

1. requests
2. plyer
You can install these dependencies using pip:

**pip install requests plyer**

