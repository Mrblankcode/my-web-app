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


# --------CREATOR SECTION--------
st.title("Creators")
# List of creators
creators = [
    {
        "name": "Guled Nassib",
        "role": "Theoretical Physicist",
        "image": "pages/guled.jpg",
        "desc": "Guled is passionate about physics and mathematics."
    },
    {
        "name": "Ali Nassib",
        "role": "computer scientist",
        "image": "pages/ali.png",
        "desc": "Ali specializes in radars and works for the FCC."
    },
    # Add more creators as needed
]

# Slider to select creator
index = st.slider("Slide to see the creators", 0, len(creators)-1, 0)

creator = creators[index]
st.image(creator["image"], caption=creator["name"], use_container_width=True)
st.subheader(creator["name"])
st.write(f"**Role:** {creator['role']}")
st.write(creator["desc"])
