import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessing objects
# Corrected filenames based on your local file names
model = joblib.load("LR_apple_products.joblib") # Corrected from .pkl to .joblib
scaler = joblib.load("scaler (1).pkl") # Updated filename
encoded_columns = joblib.load("columns (1).pkl") # Updated filename

# Page configuration
st.set_page_config(
    page_title="Apple Product Price Predictor",
    layout="centered"
)

# Title and description
st.title("Apple Product Price Predictor")
st.write("Enter the product details below to predict its current price.")

# Dropdowns for Categorical columns
product_category = st.selectbox(
    "Product Category",
    ["iPhone", "iPad", "Mac", "Watch"]
)

platform = st.selectbox(
    "Platform / Store",
    ["Amazon", "Flipkart"]
)

condition = st.selectbox(
    "Condition",
    ["New", "Renewed/Refurbished"]
)

stock_status = st.selectbox(
    "Stock Status",
    ["In Stock", "Out of Stock", "Low Stock"]
)

# Numerical inputs (min_value, max_value, and value converted to float to match step type)
launch_price_usd = st.number_input("Launch Price (USD)", 100.0, 2000.0, 429.0, step=1.0)
launch_price_inr = st.number_input("Launch Price (INR)", 10000.0, 300000.0, 79911.0, step=100.0)
current_price_usd = st.number_input("Current Price (USD)", 100.0, 2000.0, 435.81, step=0.01)
discount_pct = st.number_input("Discount Percentage (%)", -10.0, 50.0, 5.04, step=0.01)
rating = st.number_input("Rating (out of 5)", 1.0, 5.0, 4.70, step=0.1)
reviews_count = st.number_input("Reviews Count", 0, 100000, 502, step=1)

# Predict button
if st.button("Predict Current Price"):    
    # 1. Create DataFrame from user inputs
    input_data = pd.DataFrame({
        "Platform": [platform],
        "Product_Category": [product_category],
        "Condition": [condition],
        "Launch_Price_USD": [launch_price_usd],
        "Launch_Price_INR": [launch_price_inr],
        "Current_Price_USD": [current_price_usd],
        "Discount_Pct": [discount_pct],
        "Stock_Status": [stock_status],
        "Rating": [rating],
        "Reviews_Count": [reviews_count]
    })

    # 2. Perform one-hot encoding on the input data
    input_encoded = pd.get_dummies(input_data, drop_first=True)

    # 3. Reindex columns to match the training data order and features
    input_encoded = input_encoded.reindex(
        columns=encoded_columns, 
        fill_value=0
    )

    # 4. Scale the input features
    input_scaled = scaler.transform(input_encoded.values)

    # 5. Get prediction from the model
    prediction = model.predict(input_scaled)

    # Ensure price doesn't go below 0
    final_price = max(0.0, prediction[0])

    st.success(
        f"Predicted Current Price: ₹{final_price:,.2f}"
    )