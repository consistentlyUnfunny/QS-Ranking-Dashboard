import pandas as pd
import streamlit as st

@st.cache_data # Cache the data loading, so it doesn't reload every time, unless the data changes
def load_data(): 
    data = pd.read_csv("dataset/QS Ranking Cleaned.csv")
    return data