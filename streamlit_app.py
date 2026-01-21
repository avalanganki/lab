import streamlit as st 

create_page = st.Page('create_py', title='Create Page')
delete_page = st.Page('delete_py', title='Delete Page')

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title='Data manager')
pg.run()

st.Page('pages/lab1.py', title='Lab 1', icon=None, url_path=None, default=False)

