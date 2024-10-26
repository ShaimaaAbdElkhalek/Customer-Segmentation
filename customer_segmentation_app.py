import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the saved model and pipeline
model = pickle.load(open(r'C:\Users\oneway29-1-2020\AppData\Local\Programs\Python\Python312\best_model.pkl', 'rb'))

prep_pipe = pickle.load(open(r'C:\Users\oneway29-1-2020\AppData\Local\Programs\Python\Python312\prep_pipe.pkl', 'rb'))
# Streamlit app
st.title('Customer Segmentation App')

st.image('Capture.png', caption='Customer Segmentation', use_column_width=True)


# Input fields for user data
st.subheader('Input Customer Data')
education= st.selectbox('Education', ['Graduate', 'Postgraduate', 'Undergraduate'])
age = st.number_input('Age', min_value=15)
income = st.number_input('Income', min_value=0)
recency = st.number_input('Recency', min_value=0)
loyalty = st.number_input('Loyalty', min_value=0)
num_deals_purchases = st.number_input('Number of Deals Purchases', min_value=0)
num_web_purchases = st.number_input('Number of Web Purchases', min_value=0)
num_catalog_purchases = st.number_input('Number of Catalog Purchases', min_value=0)
num_store_purchases = st.number_input('Number of Store Purchases', min_value=0)
num_web_visits_month = st.number_input('Number of Web Visits per Month', min_value=0)
total_accepted_cmp = st.number_input('Total Accepted Campaigns', min_value=0)
children = st.number_input('Number of Children', min_value=0)
family_size = st.number_input('Family Size', min_value=0)
complain = st.selectbox('Complain', ['0', '1'])  # Assuming complain is categorical
response = st.selectbox('Response', ['0', '1'])  # Assuming response is categorical
marital_status = st.selectbox('Marital Status', ['Single', 'Married'])  # Add your marital status categories here
spent= st.number_input('Spent', min_value=0)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'Education': [education],
    'Age': [age],
    'Income': [income],
    'Recency': [recency],
    'Loyalty': [loyalty],
    'NumDealsPurchases': [num_deals_purchases],
    'NumWebPurchases': [num_web_purchases],
    'NumCatalogPurchases': [num_catalog_purchases],
    'NumStorePurchases': [num_store_purchases],
    'NumWebVisitsMonth': [num_web_visits_month],
    'TotalAcceptedCmp': [total_accepted_cmp],
    'Children': [children],
    'Family_Size': [family_size],
    'Complain': [complain],
    'Response': [response],
    'MaritalStatus': [marital_status],
    'Spent': [spent]
})

# Preprocess the input data
input_scaled = prep_pipe.transform(input_data)


# Predict the cluster for the input data
if st.button('Get Customer Segment'):
    cluster = model.predict(input_scaled)
    
    # Rename clusters to match customer segments
    if cluster[0] == 0:
        st.write('Predicted Customer Segment: First Customer Segment')
        st.write('### Characteristics of First Customer Segment:')
        st.write('• Low to average income, low spending')
        st.write('• Majority are Graduate/Postgraduate, very few are Undergraduate')
        st.write('• Most are Married')
        st.write('• Low response rate')
        st.write('• Have 1 child')
        st.write('• Less purchases')
        st.write('• Lowest amount spent')
        st.write('• Lowest income')
        st.write('• Median age: 42 years')
        st.write('• High loyalty')
    else:
        st.write('Predicted Customer Segment: Customer Segment 2')
        st.write('### Characteristics of Customer Segment 2:')
        st.write('• Average to high income, moderate to high spending')
        st.write('• Majority are Graduate/Postgraduate')
        st.write('• Most are Married')
        st.write('• Higher response rate')
        st.write('• No children or have 1 child')
        st.write('• More purchases')
        st.write('• Highest amount spent')
        st.write('• Highest income')
        st.write('• Median age: 48 years')
        st.write('• High loyalty')
