import streamlit as st
from openai import OpenAI

st.title("My app using secrets")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

secret_key = st.secrets.OPENAI_API_KEY
client = OpenAI(api_key=secret_key) 

uploaded_file = st.file_uploader(
    "Upload a document (.txt or .md)", type=("txt", "md")
)

question = st.text_area(
    "Now ask a question about the document!",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question:

    document = uploaded_file.read().decode()
    messages = [
        {
            "role": "user",
            "content": f"Here's a document: {document} \n\n---\n\n {question}",
        }
    ]

    # Generate an answer using the OpenAI API.
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

    st.write_stream(stream)
    