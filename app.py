import streamlit as st
import openai
import os

# API key (from Streamlit secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Product Description Generator")

name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

def fallback_description(name, brand, features, price):
    brand_text = brand if brand else "a well-known brand"
    price_text = price if price else "not specified"

    return f"""
{name} by {brand_text} is designed to meet everyday needs with comfort and reliability.
It comes with features like {features}, which make it suitable for regular use.
The product focuses on durability, ease of use, and practical performance.

It can be used in daily routines such as work, travel, casual outings, or home use,
depending on the product type. The design aims to provide long-term comfort
while maintaining consistent quality over time.

Overall, this product offers good value for money and is a dependable option
for users looking for functionality and balanced performance.
Price details: {price_text}.
"""

def generate_description(name, brand, features, price):
    prompt = f"""
Write a detailed and natural product description.

Product: {name}
Brand: {brand if brand else "Not specified"}
Features: {features}
Price: {price if price else "Not specified"}

Guidelines:
- Explain benefits in simple language
- Use real-life use cases
- Keep tone natural and human
- Minimum 100 words
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception:
        # fallback if API fails
        return fallback_description(name, brand, features, price)

if st.button("Generate"):
    if not name or not features:
        st.warning("Please enter product name and features.")
    else:
        description = generate_description(name, brand, features, price)
        st.subheader("Generated Description")
        st.write(description)

        wc = len(description.split())
        st.write("Word count:", wc)

        if wc < 70:
            st.warning("Description is short, but acceptable.")
        elif wc > 180:
            st.warning("Description is slightly long.")
        else:
            st.success("Description length is good.")
