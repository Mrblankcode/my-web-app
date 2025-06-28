import streamlit as st
import os

st.set_page_config(page_title="AboutMe", page_icon=":tada:", layout="wide")


# --------HEADER SECTION--------
st.subheader("Hi, I'm Guled, a rising theoretical physicist :wave:")
st.title("My Webpage")
st.write("I am passionate about physics and mathematics, and I am currently pursuing a degree in theoretical physics.")
st.write("I am also interested in programming and data science, and I am always looking for new challenges to tackle.")


st.write("This is a picture of me:")
image_path = "pages/guled.jpg"
if os.path.exists(image_path):
    st.image(image_path, caption="Guled's picture", use_container_width=True)
else:
    st.warning(f"Image file '{image_path}' not found.")

url = "http://www.pioneerscitech.com/u/nassiba"
st.markdown(
    f"Check out this [link]({url}) to my father's science and technology website!")
url2 = "https://www.youtube.com/@gulednassib7360"
st.markdown(
    f"Check out this [link]({url2}) to my YouTube channel!")

# --------DEDICATION SECTION--------
st.title("Dedication")
st.markdown("**This page is dedicated to Dr.Ali Nassib my father**")
st.write("Dr. Ali Nassib is a PhD holder in Electrical and Computer Engineering, specializing in radars and working for the FCC.")
st.image("pages/ali.png", caption="Dr. Ali Nassib", use_container_width=True)   

# --------FAMILY SLIDER SECTION--------
st.title("Family")
st.markdown("**This page is dedicated to my family**")

# List of family members
family = [
    {
        "name": "Guled Nassib",
        "role": "Theoretical Physicist",
        "image": "pages/guled.jpg",
        "desc": "Guled is passionate about physics and mathematics."
    },
    {
        "name": "Koshin Nassib",
        "role": "Student",
        "image": "pages/koshin.jpg",
        "desc": "Koshin wants to grow up to be a Theoretical Physist."
    },
    {
        "name": "Muna Nassib",
        "role": "Student",
        "image": "pages/muna.jpg",
        "desc": "Muna is passionate to be a Doctor."
    },
    {
        "name": "Dini Nassib",
        "role": "Student",
        "image": "pages/dini.jpg",
        "desc": "Dini is curious about the world and wants to grow up to be an astrophysist."
    },
    {
        "name": "Dr. Ali Nassib",
        "role": "PhD in Electrical and Computer Engineering",
        "image": "pages/ali.png",
        "desc": "Dr. Ali specializes in radars and works for the FCC."
    },
]

# Slider to select family member
index = st.slider("Slide to see my family members", 0, len(family)-1, 0)

member = family[index]
st.image(member["image"], caption=member["name"], use_container_width=True)
st.subheader(member["name"])
st.write(f"**Role:** {member['role']}")
st.write(member["desc"])