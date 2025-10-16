import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("Navigation 📋")
    st.write("Welcome to my interactive app!")
    st.write("---")
    st.info("This app demonstrates various Streamlit features including user input, data visualization, and recommendations.")

# Main content
st.title("My First Streamlit App 🚀")
st.markdown("### Welcome! Let's explore some interactive features")

# Section 1: User Input
st.header("👋 Personal Greeting")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("What's your name?", placeholder="Enter your name here")
    if st.button("Say hello", type="primary"):
        if name:
            st.success(f"Hello, {name}! 👋 Great to meet you!")
        else:
            st.warning("Please enter your name first! 😊")

with col2:
    age = st.slider("How old are you?", 0, 100, 25)
    st.metric(label="Your Age", value=f"{age} years")
    
    # Fun age-based message
    if age < 18:
        st.info("🎓 Youth is the time to explore!")
    elif age < 65:
        st.info("💼 Prime time of life!")
    else:
        st.info("🌟 Wisdom and experience!")

st.write("---")

# Section 2: Data Visualization
st.header("📊 Random Data Visualization")
st.markdown("Here's a randomly generated line chart that refreshes on each page load:")

# Add more data points and make it prettier
num_points = st.slider("Number of data points", 10, 100, 20)
data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['Series A', 'Series B']
)
st.line_chart(data, use_container_width=True)

# Show the data table optionally
if st.checkbox("Show raw data"):
    st.dataframe(data, use_container_width=True)

st.write("---")

# Section 3: Movie Recommender
st.header("🎬 Movie Recommender")
st.markdown("Get personalized movie recommendations based on your favorite genre!")

col3, col4 = st.columns([2, 1])

with col3:
    genre = st.selectbox(
        "Pick a genre", 
        ["Sci-Fi", "Animation", "Action", "Comedy"],
        help="Select your favorite movie genre"
    )
    
    # Extended movie database
    movies = {
        "Sci-Fi": ["🎬 Inception", "🎬 The Matrix", "🎬 Interstellar", "🎬 Blade Runner"],
        "Animation": ["🎬 Toy Story", "🎬 The Lion King", "🎬 Finding Nemo", "🎬 Spirited Away"],
        "Action": ["🎬 Die Hard", "🎬 Mad Max", "🎬 John Wick", "🎬 The Dark Knight"],
        "Comedy": ["🎬 The Hangover", "🎬 Superbad", "🎬 Groundhog Day", "🎬 Step Brothers"]
    }
    
    st.success(f"**Recommended {genre} movies:**")
    for movie in movies[genre]:
        st.write(movie)

with col4:
    st.info("**Pro Tip:** 💡\n\nTry different genres to discover new movies!")
    
# Footer
st.write("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ using Streamlit | <a href='https://streamlit.io' target='_blank'>Learn More</a></p>
    </div>
    """,
    unsafe_allow_html=True
)