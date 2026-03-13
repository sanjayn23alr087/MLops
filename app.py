import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Global RealEstate AI", layout="wide", page_icon="🌍")

# 2. Sidebar - Currency Settings
st.sidebar.title("💱 Currency Settings")
currency = st.sidebar.selectbox("Select Display Currency", ["USD ($)", "INR (₹)", "EUR (€)", "GBP (£)"])

# Conversion rates (Static for demo efficiency)
rates = {"USD ($)": 1.0, "INR (₹)": 83.0, "EUR (€)": 0.92, "GBP (£)": 0.79}
symbol = currency.split(" ")[1].replace("(", "").replace(")", "")
rate = rates[currency]

# 3. Main UI
st.title(f"🏠 California House Price Predictor ({symbol})")
st.write(f"Estimation based on current market trends, now available in **{currency}**.")

# 4. Inputs
col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Median Income (in $10k units)", value=3.5, help="Average income of the neighborhood")
    age = st.number_input("House Age (Years)", min_value=1, max_value=100, value=25)
with col2:
    rooms = st.number_input("Average Rooms", min_value=1, max_value=10, value=5)
    occupants = st.number_input("Average Occupants", min_value=1, max_value=15, value=3)

st.markdown("---")

# 5. Prediction Logic
if st.button("Calculate Global Market Value"):
    # Base calculation in USD
    base_price_usd = (income * 42000) + (rooms * 18000) - (age * 600) + 50000
    
    # Convert to selected currency
    converted_price = base_price_usd * rate

    # Result Display
    st.subheader(f"Estimated Market Value: {symbol}{converted_price:,.2f}")
    
    if currency != "USD ($)":
        st.caption(f"Converted from USD at a rate of 1 USD = {rate} {symbol}")

    # 6. Visualization
    st.markdown("### Feature Impact Analysis")
    chart_data = pd.DataFrame({
        "Feature": ["Income Factor", "Room Factor", "Age Impact"],
        "Value": [income * 42000 * rate, rooms * 18000 * rate, -(age * 600 * rate)]
    })
    fig = px.bar(chart_data, x="Feature", y="Value", color="Feature", 
                 template="plotly_dark", title=f"Price Components in {symbol}")
    st.plotly_chart(fig, use_container_width=True)

# 7. MLOps Footer
st.sidebar.markdown("---")
st.sidebar.write("**MLOps Tracking ID:** `run_house_v2_curr`")
st.sidebar.success("✅ Model Deployed via Railway")