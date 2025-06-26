import streamlit as st

st.set_page_config(page_title="Projects", page_icon=":books:", layout="wide")

st.title("My Coding Projects")

st.header("1. Projectile Motion Simulation")
st.write("""
This project simulates the trajectory of a projectile under gravity.  
It visualizes how the angle and initial velocity affect the path of the projectile.
""")
st.markdown(
    "[View code on GitHub](https://github.com/yourusername/projectile-motion-simulation)")

st.header("2. Pendulum Simulation")
st.write("""
This project models the motion of a simple pendulum using physics equations.  
It helps visualize the periodic motion and energy changes in a pendulum.
""")
st.markdown(
    "[View code on GitHub](https://github.com/yourusername/pendulum-simulation)")

# Add more projects as needed
