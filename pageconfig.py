import streamlit as st

# MUST be first - before any other st commands
st.set_page_config(
    page_title="488 Labs - Data Manager",
    page_icon="🔬",
    layout="wide"
)

# Now add your header
st.markdown('# 488 Labs')
st.markdown('## :red[Ava Langanki]')

# Create pages - reference the files directly
p1 = st.Page('/workspaces/lab/Labs/lab1.py', title='Lab 1 - Document QA', icon='📄', default=False)
p2 = st.Page('lab2.py', title='Lab 2 - Document Summarizer', icon='📝', default=True)

# Create navigation
pg = st.navigation([p1, p2])

# Run the selected page
pg.run()