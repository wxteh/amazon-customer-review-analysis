import streamlit as st
import requests
import pandas as pd

# Streamlit UI elements
st.title("Alternative Product Recommendations")
product = st.selectbox('Product Category', ('Please choose your product category', 'USBCables', 'Smartphones', 'WirelessUSBAdapters'))
review = st.text_input("Enter your review")
if st.button('Submit'):
    params = dict(
        product_category=product,
        text=review
    )

    amazon_api_url = 'https://final-test-hezmcck7ba-nw.a.run.app/predict'
    response = requests.get(amazon_api_url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        #df_results = pd.DataFrame({
                        #'Product ID': list(prediction['data']['product_id'].values()),
                        #'Product Name': list(prediction['data']['product_name'].values()),
                        #'Summary': list(prediction['data']['summary'].values())
                        #})

        message = prediction['message']
        if prediction['data']:
            df_results = pd.DataFrame({
                        'Product ID': list(prediction['data']['product_id'].values()),
                        'Product Name': list(prediction['data']['product_name'].values()),
                        'Summary': list(prediction['data']['summary'].values())
                        })
            st.write(message)
            st.dataframe(data=df_results)
        else:
            st.write(message)

    else:
        st.write("Request Failed with Status Code:", response.status_code)
