import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

# Function to get weather details using OpenWeather API
def get_weather(location):
    try:
        # Build the OpenWeather API request URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=en&appid={openweather_api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            weather_desc = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            return weather_desc, temp
        else:
            return "Error: Could not retrieve weather data", None
    except Exception as e:
        return str(e), None

# Streamlit UI
st.title(" Weather App 🌤️")

location = st.text_input("Enter Location:", placeholder="e.g., New York")

if st.button("Get Weather"):
    if location:
        weather_desc, temp = get_weather(location)
        if weather_desc and temp:
            st.markdown(f"## Weather at {location}:")
            st.write(f"Description: {weather_desc}")
            st.write(f"Temperature: {temp}°C")
        else:
            st.error("Could not retrieve weather data.")
    else:
        st.error("Please enter a location.")
