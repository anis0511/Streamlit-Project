import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

#uploading data
@st.cache_data   #If the file or function inputs change, it automatically reruns and updates the cache.
def load_data():
    return pd.read_csv("Cleaned_Education_Costs.csv")

df = load_data()

# Calculate the whole total cost
if 'Total_Cost_USD' not in df.columns:
    df["Total_Cost_USD"] = (
        df["Tuition_USD"] +
        df["Rent_USD"] * 12 * df["Duration_Years"] +
        df["Visa_Fee_USD"] +
        df["Insurance_USD"]
    )

