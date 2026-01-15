import streamlit as st
import openai
import os

# Read API key from environment / Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Product Description Generator")

st.title("Product Description Generator")

# Input fields
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

def generate_description(name, brand, features, price):
    prompt = f"""
Write a detailed and natural product description for the following item.

Product name: {name}
Brand: {brand if brand else "Not specified"}
Key features: {features}
Price: {price if price else "Not specified"}

Guidelines:
- Description should be 90 to 130 words
- Write like a human product expert
- Do not repeat sentences
- Focus on real-life usage and benefits
- Do not use bullet points
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )

    return response.choices[0].message["content"].strip()

# Button logic
if st.button("Generate"):
    if not product_name or not features:
        st.error("Please enter product name and key features.")
    else:
        try:
            description = generate_description(
                product_name,
                brand,
                features,
                price
            )

            st.subheader("Generated Description")
            st.write(description)

            word_count = len(description.split())
            st.write(f"Word count: {word_count}")

            if word_count < 80:
                st.warning("Description is a bit short.")
            elif word_count > 150:
                st.warning("Description is too long.")
            else:
                st.success("Description length is good.")

        except Exception as e:
            st.error("Error generating description. Please try again later.")
