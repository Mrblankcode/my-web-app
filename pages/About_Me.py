import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# --------HEADER SECTION--------
st.subheader("Hi, I'm Guled, a rising theoretical physicist :wave:")
st.title("My Webpage")
st.write("I am passionate about physics and mathematics, and I am currently pursuing a degree in theoretical physics.")
st.write("I am also interested in programming and data science, and I am always looking for new challenges to tackle.")

# Comment out the image line for testing
st.write("[Credit to my dad>](http://www.pioneerscitech.com/upload/2018/07/alixxx_200_200.png)")
url = "http://www.pioneerscitech.com/u/nassiba"
st.markdown(
    f"Check out this [link]({url}) to my father's science and technology website!")
