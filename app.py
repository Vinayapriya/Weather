import os
import requests
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def get_weather_openweather(location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=en&appid={openweather_api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_desc = weather_data['weather'][0]['description']
            temp_celsius = weather_data['main']['temp']
            temp_fahrenheit = temp_celsius * 9/5 + 32  
            chance_of_rain = weather_data.get('rain', {}).get('1h', 0)  
            return weather_desc, temp_celsius, temp_fahrenheit, chance_of_rain
        else:
            return None, None, None, None
    except Exception as e:
        return None, None, None, None


def get_weather_gemini(location, weather_desc, temp_celsius, temp_fahrenheit, chance_of_rain):
    try:
        
        prompt = f"The current weather in {location} is {weather_desc}. The temperature is {temp_fahrenheit:.1f} degrees Fahrenheit ({temp_celsius:.1f} degrees Celsius). There is a {chance_of_rain}% chance of rain today."
        
       
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config
        )

        
        chat_session = model.start_chat(history=[])

        
        response = chat_session.send_message(prompt)

        return response.text
    except Exception as e:
        return str(e)


st.title(" Weather App 🌤")


location = st.text_input("Enter Location:", placeholder="e.g., New York")

if st.button("Get Weather"):
    if location:
        
        weather_desc, temp_celsius, temp_fahrenheit, chance_of_rain = get_weather_openweather(location)
        
        if weather_desc and temp_celsius is not None:
           
            st.markdown(f"## Weather Data for {location}:")
            st.write(f"**Description:** {weather_desc.capitalize()}")
            st.write(f"**Temperature:** {temp_celsius:.1f}°C / {temp_fahrenheit:.1f}°F")
            st.write(f"**Chance of Rain:** {chance_of_rain}%")
            
            
            gemini_response = get_weather_gemini(location, weather_desc, temp_celsius, temp_fahrenheit, chance_of_rain)
            
            st.markdown(f"## Gemini Response:")
            st.write(gemini_response)
        else:
            st.error("Could not retrieve weather data.")
    else:
        st.error("Please enter a location.")
