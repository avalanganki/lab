import streamlit as st

st.title("My app using secrets")

secret_key = st.secrets.OPENAI_API_KEY
st.write("Here is my secret key:", secret_key)
st.write("And here again!", st.secrets("OPENAI_API_KEY"))