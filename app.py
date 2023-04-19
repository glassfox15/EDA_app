import streamlit as st
# python3 -m streamlit run /Users/jake/Python/streamlit_project/app.py (command in terminal)

st.title('Stats 21 - Streamlit Project')
st.markdown("For example, this here  is a **bold text**")

st.sidebar.title('title of sidebar')

agree = st.checkbox('Click me')

if agree:
    st.write('Great!')
    st.markdown('This is *italic* text')


side_check = st.sidebar.checkbox('Check box')
if side_check:
    st.sidebar.write('Sidebar checkbox has been clicked')
# st.write like universal print, can print text, objects, etc

