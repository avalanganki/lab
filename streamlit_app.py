import streamlit as st

st.set_page_config(
    page_title="488 Labs - Data Manager",
    page_icon="🔬",
    layout="wide"
)

st.markdown('# 488 Labs')
st.markdown('## :red[Ava Langanki]')

p1 = st.Page('lab1.py', title='Lab 1 - Document QA', icon='📄', default=False)
p2 = st.Page('lab2.py', title='Lab 2 - Document Summarizer', icon='📝', default=True)

pg = st.navigation([p1, p2])

pg.run()