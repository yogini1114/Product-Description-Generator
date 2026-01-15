import streamlit as st
import random

st.title("Product Description Generator")

# -------- INPUTS --------
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features (comma separated)")
price = st.text_input("Price (optional)")

# -------- HELPER FUNCTION --------
def generate_description(name, brand, features, price):
    sentences = []

    # intro
    intro_templates = [
        f"{name} is a well-designed product meant for everyday use.",
        f"The {name} is created to meet daily usage needs.",
        f"{name} offers a balance of usability and performance."
    ]
    sentences.append(random.choice(intro_templates))

    # brand
    if brand:
        sentences.append(f"It is manufactured by {brand}, a brand known for reliability.")

    # features
    feature_list = [f.strip() for f in features.split(",") if f.strip()]
    for feat in feature_list:
        sentences.append(f"The product includes {feat}, which improves overall user experience.")

    # usage
    usage_templates = [
        "It can be comfortably used at home as well as outdoors.",
        "This product is suitable for work, travel, and personal use.",
        "Its design supports long-term usage without discomfort."
    ]
    sentences.append(random.choice(usage_templates))

    # price
    if price:
        sentences.append(f"The product is priced at {price}, offering good value for money.")
    else:
        sentences.append("Pricing details are currently not available.")

    # conclusion
    sentences.append("Overall, this product is a practical choice for users looking for quality and dependability.")

    return " ".join(sentences)

# -------- BUTTON --------
if st.button("Generate"):
    if not product_name or not features:
        st.error("Product name and features are required.")
    else:
        description = generate_description(product_name, brand, features, price)

        st.subheader("Generated Description")
        st.write(description)

        word_count = len(description.split())
        st.write("Word count:", word_count)

        if word_count < 60:
            st.error("Description is too short")
        elif word_count > 140:
            st.error("Description is too long")
        else:
            st.success("Description length is acceptable")
