import streamlit as st

st.title("My First Streamlit App 🚀")

name = st.text_input("What's your name?")
if st.button("Say hello"):
    st.write(f"Hello, {name or 'there'}! 👋")

age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old.")

import pandas as pd
import numpy as np
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)
st.line_chart(data)


st.title("Simple Movie Recommender 🎬")

movies = ["Inception", "The Matrix", "Interstellar", "Toy Story", "The Lion King"]
genre = st.selectbox("Pick a genre", ["Sci-Fi", "Animation"])

if genre == "Sci-Fi":
    st.write("Recommended:", movies[:3])
else:
    st.write("Recommended:", movies[3:])