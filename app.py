import streamlit as st
import requests
import pandas as pd
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''




url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

st.title("Taxi Fare Prediction")

pickup_d = st.date_input("date")
pickup_t = st.time_input("time")
pickup_date = f"{pickup_d} {pickup_t}"
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802)
passenger_count = st.slider("Passenger count", 1, 8, 1)


url = 'https://taxifare.lewagon.ai/predict'
params = {
    "pickup_datetime": pickup_date,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
prediction = response.json()
st.write(prediction)

if response.status_code == 200:
    fare = prediction['fare']
    st.write(f"The predicted fare is: ${fare:.2f}")
else:
    st.write("Error in retrieving prediction")


st.map(pd.DataFrame({
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
}))
