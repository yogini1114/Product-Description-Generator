import streamlit as st
import openai
import os

# -------------------------------
# Configuration
# -------------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Product Description Generator")
st.title("Product Description Generator")

# -------------------------------
# Input Fields
# -------------------------------
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

# -------------------------------
# Fallback Description Generator
# -------------------------------
def fallback_description(name, brand, features, price):
    desc = f"{name} is designed to meet everyday needs and practical use. "

    if brand:
        desc += f"It is manufactured by {brand}, a brand known for reliability and quality. "

    if features:
        desc += f"The product offers features such as {features}, which improve overall usability. "

    desc += (
        "The design focuses on comfort, durability, and ease of use, "
        "making it suitable for regular use in different situations. "
    )

    if price:
        desc += f"It is available at a price of {price}, providing good value for money."
    else:
        desc += "Pricing information is currently not specified."

    return desc

# -------------------------------
# AI Description Generator
# -------------------------------
def ai_description(name, brand, features, price):
    prompt = f"""
Write a detailed and natural product description.

Product Name: {name}
Brand: {brand if brand else 'Not specified'}
Key Features: {features}
Price: {price if price else 'Not specified'}

Write a paragraph of at least 90 words.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# -------------------------------
# Generate Button
# -------------------------------
if st.button("Generate"):
    if not product_name or not features:
        st.error("Please enter at least Product Name and Key Features.")
    else:
        try:
            description = ai_description(product_name, brand, features, price)
        except Exception:
            description = fallback_description(product_name, brand, features, price)

        # -------------------------------
        # Output
        # -------------------------------
        st.subheader("Generated Description")
        st.write(description)

        word_count = len(description.split())
        st.write("Word count:", word_count)

        if word_count < 70:
            st.warning("Description is short, but acceptable for basic usage.")
        elif word_count > 150:
            st.warning("Description is slightly long.")
        else:
            st.success("Description length is good.")
