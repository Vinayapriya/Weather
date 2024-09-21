# Weather App with OpenWeather, Gemini, and Pathway Integration

This is a simple weather app that fetches weather information using the OpenWeather API and provides a response using the Gemini API. The data is saved in JSON Lines format using the Pathway library.

## Features

- Fetches current weather data for a given location using OpenWeather API.
- Provides a natural language description of the weather using the Gemini API.
- Saves the weather data and Gemini response in JSON Lines format using Pathway.

## Tech Stack

- **Python**: Core programming language.
- **Streamlit**: For the web interface.
- **OpenWeather API**: To fetch real-time weather data.
- **Gemini API**: For generating a natural language description of the weather.
- **Pathway**: To save the data in JSON Lines format.
- **Dotenv**: To manage environment variables.

## Requirements

- Python 3.7+
- Streamlit
- OpenWeather API key
- Gemini API key
- Pathway library
- Google Generative AI Python SDK
- Requests library
- Dotenv library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file in the root of your project and add your API keys:
   ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```
## Running the App
1.To run the app, execute the following command:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to http://localhost:8501.
3. Enter a location and click on the "Get Weather" button to see the current weather and Gemini response.

## File Structure
   ```code
   weather-app/
   ├── app.py              # Main Python file to run the app
   ├── requirements.txt    # Python dependencies
   ├── .env                # Environment variables (not included in the repo)
   └── README.md           # This readme file
   ```

## Usage
1.**Get Weather Data**: Enter a location (e.g., "New York") and click on "Get Weather". The app will display:

   -Temperature in Celsius and Fahrenheit
   -Chance of rain
2.**Gemini Response**: The app will generate a natural language weather description using the Gemini API.

3.**Saving Data**: The weather data and Gemini response are saved in JSON Lines format, stored in files named after the location (e.g., 
  New_York_weather.jsonl and New_York_gemini_response.jsonl).

## Demo
 [streamlit-app-2024-09-21-22-09-30.webm](https://github.com/user-attachments/assets/69aff1dd-6c4b-46c9-a818-05761f8f9733)

 ## License
 This project is licensed under the MIT License. See the LICENSE file for details.




