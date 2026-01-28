import streamlit as st
from openai import OpenAI

st.title("Document QA With Secret")
secret_key = st.secrets.OPENAI_API_KEY
client = OpenAI(api_key=secret_key) 

st.sidebar.title("Options")
options = st.sidebar.selectbox(
    'How would you like it to be answered?',
    ('100 Words Basic', 'Two Paragraphs', '5 Bullet Points')
)
if options == '100 Words Basic':
    prompt_instruction = "Summarize this document in exactly 100 words"
elif options == 'Two Paragraphs':
    prompt_instruction = "Summarize this document in two connecting paragraphs"
elif options == '5 Bullet Points':
    prompt_instruction = "Summarize this document in five bullet points"

model_list = ['gpt-4o-mini', 'gpt-4o-nano']
selected_model = st.sidebar.selectbox('Select Model', model_list)
uploaded_file = st.file_uploader(
    "Upload a document (.txt or .md)", type=("txt", "md")
)

if uploaded_file and options:

    document = uploaded_file.read().decode()
    messages = [
        {
            "role": "user",
            "content": f"{prompt_instruction}\n\nDocument: {document}",
        }
    ]

    # Generate an answer using the OpenAI API.
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

    st.write_stream(stream)

    #lab 2 p.C instructions
    # provide user with options 
    # summarize in 100 words
    # summarize in two connecting paragraphs
    # summarize in 5 bullet 
    # let user select btwn models (mini / nano)
    # have a checkbox for 'advanced model'
    