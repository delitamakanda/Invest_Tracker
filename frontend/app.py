import os
import streamlit as st
import pandas as pd
import requests

# API_URL = "http://localhost:8000/api"
API_URL = "https://invest-api-946790860424.europe-west9.run.app/api"
PORTFOLIO_ID = 1

st.set_page_config(page_title="Portfolio Management", layout="wide")

st.header("Portfolio Management")

if st.button("Refresh"):
    st.cache_data.clear()
    st.success("Portfolio data refreshed.")


@st.cache_data(ttl=3600)
def get_positions():
    response = requests.get(f"{API_URL}/portfolios/{PORTFOLIO_ID}/positions/")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error(f"Error fetching portfolio positions: {response.status_code} - {response.text}")
        return pd.DataFrame()


@st.cache_data(ttl=3600)
def get_portfolio_value():
    response = requests.get(f"{API_URL}/portfolios/{PORTFOLIO_ID}/value/")
    if response.status_code == 200:
        return response.json()["value"]
    else:
        st.error(f"Error fetching portfolio value: {response.status_code} - {response.text}")
        return 0


positions_df = get_positions()
portfolio_value = get_portfolio_value()

if not positions_df.empty:
    st.subheader("Positions")
    st.dataframe(positions_df)
    st.subheader("Portfolio Value")
    pie_data = positions_df.groupby('asset')['quantity'].sum()
    st.pyplot(pie_data.plot.pie(autopct='%1.1f%%', figsize=(6, 6)).figure)
    
    st.metric("Portfolio Value", f"{portfolio_value:.2f}€")
else:
    st.info("No positions found for this portfolio.")
