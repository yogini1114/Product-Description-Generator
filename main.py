from openai import OpenAI
import os

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("\nEnter product details\n")

# Taking input from user
name = input("Product name: ")
brand = input("Brand (optional): ")
features = input("Key features: ")
price = input("Price (optional): ")

# Handling empty inputs
if name == "":
    name = "Unknown Product"

if brand == "":
    brand = "Generic Brand"

if features == "":
    features = "Standard features"

if price == "":
    price = "Price not available"

# Reading prompt file
with open("prompts/general.txt", "r") as file:
    prompt = file.read()

# Filling prompt
final_prompt = prompt.format(
    name=name,
    brand=brand,
    features=features,
    price=price
)

# Function to generate description
def generate_description(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# Generate output
description = generate_description(final_prompt)

print("\nGenerated Product Description:\n")
print(description)

# Simple quality check
word_count = len(description.split())
print("\nWord count:", word_count)

if word_count < 50:
    print("Description is short")
else:
    print("Description generated successfully")
