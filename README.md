# Apple Product Price Predictor

This project implements a machine learning model to predict the current price of Apple products based on various features such as launch price, discount percentage, rating, and other categorical information.

## Project Overview

The goal of this project is to build a predictive model that can estimate the current market price of different Apple products. This can be useful for buyers and sellers to gauge fair prices.

## Dataset

The dataset used for this project contains information about Apple products from 2020 to 2026, including:
- `Date`: Date of the price entry.
- `Platform`: E-commerce platform (e.g., Amazon, Flipkart).
- `Product_Category`: Product type (e.g., iPhone, iPad, Mac, Watch).
- `Model_Name`: Specific model of the product.
- `Condition`: Product condition (New, Renewed/Refurbished).
- `Launch_Price_USD`, `Launch_Price_INR`: Original launch prices in USD and INR.
- `Current_Price_USD`, `Current_Price_INR`: Current prices in USD and INR.
- `Discount_Pct`: Discount percentage.
- `Sale_Event`: Indication of a sale event (e.g., Big Billion Days, Great Indian Festival).
- `Stock_Status`: Product stock availability.
- `Rating`: Average customer rating.
- `Reviews_Count`: Number of reviews.

## Data Preprocessing

1.  **Handling Missing Values**: Missing values in the `Sale_Event` column were filled with 'No Event'.
2.  **Duplicate Removal**: No duplicate rows were found in the dataset.
3.  **One-Hot Encoding**: Categorical features (`Platform`, `Product_Category`, `Model_Name`, `Condition`, `Sale_Event`, `Stock_Status`, `Date`) were converted into numerical format using one-hot encoding.
4.  **Feature Scaling**: Numerical features were scaled using `StandardScaler` to normalize their ranges.
5.  **Feature and Target Split**: `Current_Price_INR` was chosen as the target variable (`y`), and all other processed features were used as independent variables (`X`).

## Model Training

A `LinearRegression` model from `sklearn` was used for predicting the current price. The model was trained on the preprocessed and scaled dataset.

-   **R² Score**: The model achieved an R² score of approximately 0.998, indicating a very strong fit to the data.

## Streamlit Application

A Streamlit web application (`app2.py`) has been developed to provide an interactive interface for predicting Apple product prices.

### How to Run the Streamlit App

1.  **Save the Code**: Copy the Streamlit code provided previously into a file named `app2.py`.
2.  **Download Model Artifacts**: Ensure you have the following files in the same directory as `app2.py`:
    -   `LR_apple_products.joblib` (the trained model)
    -   `scaler (1).pkl` (the StandardScaler object)
    -   `columns (1).pkl` (the list of column names used during training)
    
    You can download these from your Colab notebook if you haven't already.
3.  **Install Dependencies**: Make sure you have the necessary libraries installed. You can do this by running:
    ```bash
    pip install streamlit pandas scikit-learn joblib
    ```
4.  **Run the App**: Open your terminal or command prompt, navigate to the directory where `app2.py` and the model files are saved, and run:
    ```bash
    streamlit run app2.py
    ```
5.  **Interact**: Your web browser will open, displaying the Apple Product Price Predictor application. You can then input product details and get a predicted current price.
