import streamlit as st
import openai
import os

# Page title
st.title("Product Description Generator")

st.write("Enter product details to generate a short description.")

# API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User inputs
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

# -------- FILE PATH FIX (IMPORTANT) --------
current_dir = os.path.dirname(__file__)
prompt_file = os.path.join(current_dir, "prompts", "general.txt")

# Load prompt
with open(prompt_file, "r") as f:
    base_prompt = f.read()

# Button
if st.button("Generate"):

    if product_name == "" or features == "":
        st.warning("Please fill product name and features.")
    else:
        if brand == "":
            brand = "Generic Brand"

        if price == "":
            price = "Not specified"

        final_prompt = base_prompt.format(
            name=product_name,
            brand=brand,
            features=features,
            price=price
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": final_prompt}]
        )

        description = response.choices[0].message.content

        st.subheader("Generated Description")
        st.write(description)

        word_count = len(description.split())
        st.write("Word count:", word_count)

        if word_count < 60:
            st.error("Description is too short")
        elif word_count > 120:
            st.error("Description is too long")
        else:
            st.success("Description length is acceptable")
