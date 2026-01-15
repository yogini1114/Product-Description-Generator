import streamlit as st
import openai
import os

# Read API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Product Description Generator")

# Inputs
name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

def generate_description(name, brand, features, price):
    prompt = f"""
Product name: {name}
Brand: {brand if brand else "Not specified"}
Key features: {features}
Price: {price if price else "Not specified"}

Instructions:
- Explain how the features benefit the user
- Use real-life use cases
- Keep tone natural and human
- Write a detailed description (minimum 100 words)
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content


if st.button("Generate"):
    if not name or not features:
        st.error("Please enter product name and features.")
    else:
        description = generate_description(name, brand, features, price)

        st.subheader("Generated Description")
        st.write(description)

        word_count = len(description.split())
        st.write("Word count:", word_count)

        if word_count < 100:
            st.warning("Description is a bit short.")
        else:
            st.success("Description length looks good.")
