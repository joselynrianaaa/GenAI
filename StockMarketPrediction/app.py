import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from tensorflow.keras.models import load_model
import streamlit as st


start = '2018-01-01'
end = '2023-01-01'

st.title('Stock Trend Prediction')

user_input = st.text_input("Enter Stcok Ticker" , 'AAPL')
df = data.DataReader(user_input , 'yahoo' , start , end)

st.subheader('Data from 2018 - 2023')
st.write(df.describe())