Product Description Generator Project

Introduction

This project is a simple Python-based application that generates product descriptions for an online shopping platform.  
The user provides basic product details such as name, brand, features, and price, and the program generates a readable product description using a predefined text template.



Objective
The main objective of this project is to:
- Take product details from the user
- Generate a meaningful product description
- Display the description in a clean and readable format

This project helps understand how text templates and external APIs can be used in real-world applications.


How the Project Works
1. The user enters product details through the terminal.
2. A general description template is loaded from a text file.
3. The entered values are inserted into the template.
4. The completed prompt is sent to the OpenAI API.
5. The generated product description is displayed to the user.
6. A simple word count check is performed.



Project Structure


Input Details
The program asks the user for the following information:
- Product Name
- Brand (optional)
- Key Features
- Price (optional)

If any optional field is left empty, the program automatically assigns a default value.



Prompt Design
A single general prompt template is used so that the program can work for any type of product such as electronics, clothing, furniture, books, or household items.

The prompt is written in simple language to keep the output easy to understand.


Output
The output is a product description written in clear and simple English.  
The program also displays the total word count of the generated description.



Error Handling
- If the user does not enter optional details, default values are used.
- The program does not crash due to missing inputs.
- File handling is managed carefully to avoid runtime errors.

---

How to Run the Project
1. Install required library.

2. Set your OpenAI API key as an environment variable.

3. Run the program.

4. Enter the product details when prompted.

Learning Outcome
Through this project, the following concepts were learned:
- Python input handling
- File handling in Python
- Using text templates
- Basic API integration
- Writing clean and readable code



Conclusion
This project demonstrates a basic and practical use case of Python for generating product descriptions.  
It is simple, flexible, and can be extended further for additional features if required.



