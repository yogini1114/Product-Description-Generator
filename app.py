import streamlit as st
import openai
import os

# Page heading
st.title("Product Description Generator")
st.write("Enter product details to generate a simple description.")

# API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User inputs
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

# Load prompt file safely
current_dir = os.path.dirname(__file__)
prompt_path = os.path.join(current_dir, "prompts", "general.txt")

with open(prompt_path, "r") as f:
    base_prompt = f.read()

# Button click
if st.button("Generate"):

    if product_name == "" or features == "":
        st.warning("Please enter product name and key features.")
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

        # Try OpenAI API, else fallback
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": final_prompt}]
            )
            description = response.choices[0].message.content

        except:
            # Fallback description (VERY IMPORTANT)
            description = f"""
{product_name} by {brand} is designed for everyday use.
It offers features such as {features}, making it practical and reliable.
The product delivers good performance and value for users.
Price details: {price}.
"""

        # Output
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
