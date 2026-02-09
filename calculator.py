# import streamlit as st
# st.title('My First Streamlit App')
# st.write('Hello, Streamlit!')
# name = st.text_input('Enter your name:')
# if name:
#     st.success(f'Welcome, {name}!')

import streamlit as st

st.title("🧮 Simple Calculator")

# Number inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selector
operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"✅ Result: {result}")