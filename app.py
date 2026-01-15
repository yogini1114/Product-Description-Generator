import streamlit as st

st.set_page_config(page_title="Product Description Generator")

st.title("Product Description Generator")

# Inputs
product_name = st.text_input("Product Name")
brand = st.text_input("Brand (optional)")
features = st.text_area("Key Features")
price = st.text_input("Price (optional)")

if st.button("Generate"):
    # Handle empty inputs
    if not product_name:
        product_name = "This product"
    if not brand:
        brand = "a trusted brand"
    if not features:
        features = "useful everyday features"
    if not price:
        price = "Not specified"

    # Fallback description (INTENTIONALLY LONG)
    description = f"""
    {product_name} by {brand} is designed to meet everyday needs with a focus on comfort,
    performance, and reliability. It includes features such as {features}, which help improve
    usability and overall user experience. The product is suitable for daily activities like
    work, travel, and personal use, making it a practical choice for a wide range of users.
    Its durable build and thoughtful design ensure long-term usage and value for money.
    Price details: {price}.
    """

    # Output
    st.subheader("Generated Description")
    st.write(description)

    # Word count check
    word_count = len(description.split())
    st.write("Word count:", word_count)

    if word_count < 60:
        st.error("Description is too short")
    elif word_count > 120:
        st.error("Description is too long")
    else:
        st.success("Description length is acceptable")
