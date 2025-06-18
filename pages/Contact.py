import streamlit as st

st.set_page_config(page_title="Contact", page_icon=":mailbox:", layout="wide")

st.title("Contact")

st.write("Fill out the form below to contact me:")

contact_form = """
<form action="https://formsubmit.co/bruvmeguled@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)