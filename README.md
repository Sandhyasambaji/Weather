# 🌤️ Smart Weather Forecast App

A simple and interactive **Streamlit web app** that provides **real-time weather updates** and **quick safety precautions** based on the weather condition of any city.  
The app fetches data from the **OpenWeatherMap API** and displays temperature, humidity, and weather descriptions in an easy-to-understand format.

---

## 🚀 Features

- 🌍 Get real-time weather details for any city  
- 🌡️ Displays current temperature (°C) and humidity (%)  
- ⚠️ Shows quick and useful precautions according to weather conditions  
- 🖥️ Simple and clean Streamlit user interface  

---

## 🧩 How It Works

1. Enter your **city name** in the input box.  
2. The app sends a request to the **OpenWeatherMap API**.  
3. It retrieves the **temperature, humidity**, and **weather condition**.  
4. Displays a short list of **precautions** suited for that weather.

---

## 🛠️ Technologies Used

- **Python**  
- **Streamlit**  
- **Requests Library**  
- **OpenWeatherMap API**

---

## ⚙️ Installation and Setup

1. Clone the repository
2. Install the required libraries:
     pip install streamlit requests
3.Run the app:
     streamlit run weather.py
4.Open the local URL displayed in your terminal

## 🔑 API Key Setup

This app requires an API key from OpenWeatherMap.
You can get your free key from https://openweathermap.org/api
Replace this line in your code with your key:
       api_key = "your_api_key_here"
