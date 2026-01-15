import streamlit as st
import openai
import os
import random

# API key from environment / secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Product Description Generator")

# User Inputs
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features (comma separated)")
price = st.text_input("Price (optional)")

if not brand:
    brand = "a well-known brand"

if not price:
    price = "not specified"

def generate_description(name, brand, features, price):
    styles = [
        "Write in a simple and informative tone.",
        "Write in a user-friendly and practical tone.",
        "Write like an e-commerce product listing.",
        "Write focusing on daily usage and comfort."
    ]

    prompt = f"""
    Write a detailed product description for the following product.

    Product Name: {name}
    Brand: {brand}
    Key Features: {features}
    Price: {price}

    Instructions:
    - {random.choice(styles)}
    - Do not repeat sentences.
    - Make the description specific to the product.
    - Minimum length: 80 words.
    - Explain how the product can be used in real life.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()

# Button
if st.button("Generate"):
    if not product_name or not features:
        st.error("Please enter product name and features")
    else:
        description = generate_description(
            product_name,
            brand,
            features,
            price
        )

        st.subheader("Generated Description")
        st.write(description)

        wc = len(description.split())
        st.write("Word count:", wc)

        if wc < 70:
            st.warning("Description is a bit short")
        else:
            st.success("Description length is good")
