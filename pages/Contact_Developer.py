import streamlit as st
import streamlit.components.v1 as components

st.write("Use the form below to get in touch with the Developer.")

st.markdown("<h1 style='text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)

# Load the content of the external URL using iframe
iframe_code = '<iframe src="https://formsubmit.co/el/jidexe" width="800" height="600"></iframe>'
components.html(iframe_code, height=600)
