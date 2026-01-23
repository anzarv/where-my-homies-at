import streamlit as st

# This puts a title on your app screen
st.title("The Magic Box")

# This creates a box for you to type in
user_input = st.text_input("Type something here:")

# This shows the output only after you type something
if user_input:
    st.write("The Magic Box says:")
    st.header(user_input.upper()) # This makes your input BIG and LOUD

