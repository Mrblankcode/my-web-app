import streamlit as st

st.set_page_config(page_title="My Web App",
                   page_icon=":guardsman:", layout="wide")
st.title("My Web App")
st.write("Hello my name is Guled Nassib and I am a theoretical physicist.")
st.write("This is a simple web app about me and my work.")
st.write("I am currently working on a project about projectile motion.")
st.write("I am using Python and the module Streamlit to create this web app.")

# Display the image with a caption
# Use the correct file path or an online URL
st.image("http://www.pioneerscitech.com/upload/2018/07/alixxx_200_200.png",
         caption="Ali Nassib", use_container_width=True)
