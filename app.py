
import streamlit as st
import pandas as pd

st.set_page_config(page_title="🌾 FarmGuard: Crop Yield Analyzer", layout="centered")
st.title("🌾 FarmGuard: Crop Yield Analyzer")

df = pd.read_csv("crop_yield.csv")
district = st.selectbox("Select District", df["District"].unique())
crop = st.selectbox("Select Crop", df["Crop"].unique())

filtered = df[(df["District"] == district) & (df["Crop"] == crop)]
st.subheader(f"{crop} Yield in {district} Over the Years")
st.line_chart(filtered.set_index("Year")["Yield"])

avg = filtered["Yield"].mean()
st.success(f"Average Yield: {avg:.2f} kg/ha")
