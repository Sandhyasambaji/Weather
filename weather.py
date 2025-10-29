import streamlit as st
import requests

st.title("🌤️ Smart Weather Forecast App")
st.write("Get real-time weather updates and quick safety precautions based on the weather condition.")

city = st.text_input("Enter the city name:")

api_key = "1432a1c5e57a0ba064c48766334cd1e5"

if st.button("Get Weather Details"):
    if city:
        # API call
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get('cod') == 200:
            st.subheader(f"🌆 Weather in {city.title()}")

            # Extract details
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description'].capitalize()

            # Display weather info
            st.write(f"**Condition:** {condition}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Humidity:** {humidity}%")

            # General precautions (combined)
            st.subheader("⚠️ Precautions:")

            if temp >= 40:
                st.warning("🔥 Extremely Hot Weather")
                st.markdown("""
                - Stay indoors during afternoon hours  
                - Drink water frequently  
                - Wear light cotton clothes  
                - Avoid heavy meals  
                - Use sunscreen when outside
                """)

            elif 30 <= temp < 40:
                st.info("🌞 Hot Weather")
                st.markdown("""
                - Keep yourself hydrated  
                - Avoid long exposure to sunlight  
                - Use sunglasses and a hat  
                - Take frequent breaks outdoors  
                - Stay in cool, ventilated places
                """)

            elif 20 <= temp < 30:
                st.success("😊 Pleasant Weather")
                st.markdown("""
                - Perfect time for outdoor activities  
                - Drink enough water  
                - Wear comfortable clothing  
                - Use sunscreen if it’s sunny  
                - Enjoy your day outdoors
                """)

            elif 10 <= temp < 20:
                st.info("🧥 Cool Weather")
                st.markdown("""
                - Wear light sweaters or jackets  
                - Drink warm liquids  
                - Avoid staying out late  
                - Keep yourself comfortable indoors  
                - Ensure proper ventilation
                """)

            else:
                st.warning("❄️ Cold Weather")
                st.markdown("""
                - Dress warmly in layers  
                - Keep your head and hands covered  
                - Drink warm fluids  
                - Stay indoors during chilly hours  
                - Avoid cold water and icy areas
                """)

        else:
            st.error(f"City not found: {data.get('message', '')}")
    else:
        st.warning("Please enter a city name.")
