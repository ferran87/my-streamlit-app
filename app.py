import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Google Sheets Configuration
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Function to connect to Google Sheets
@st.cache_resource
def get_google_sheet():
    """Connect to Google Sheets using credentials from Streamlit secrets"""
    try:
        # Get credentials from Streamlit secrets
        credentials_dict = st.secrets["gcp_service_account"]
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, SCOPE)
        client = gspread.authorize(credentials)
        
        # Open the Google Sheet (you'll need to specify your sheet name)
        sheet_name = st.secrets.get("sheet_name", "streamlit_user_data")
        
        try:
            # Try to open existing sheet
            spreadsheet = client.open(sheet_name)
            worksheet = spreadsheet.sheet1
        except gspread.SpreadsheetNotFound:
            # Create new sheet if it doesn't exist
            spreadsheet = client.create(sheet_name)
            worksheet = spreadsheet.sheet1
            # Initialize headers
            worksheet.append_row(['timestamp', 'name', 'age', 'favorite_genre'])
            # Make it accessible
            spreadsheet.share('', perm_type='anyone', role='reader')
        
        return worksheet
    except Exception as e:
        st.error(f"Error connecting to Google Sheets: {e}")
        st.info("💡 Make sure you've set up Google Sheets credentials in Streamlit secrets!")
        return None

# Save user data to Google Sheets
def save_user_data(name, age, genre):
    try:
        worksheet = get_google_sheet()
        if worksheet:
            row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), name, age, genre]
            worksheet.append_row(row)
            return True
        return False
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# Load user data from Google Sheets
def load_user_data():
    try:
        worksheet = get_google_sheet()
        if worksheet:
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            return df
        return pd.DataFrame()
    except Exception as e:
        st.warning(f"Could not load data: {e}")
        return pd.DataFrame()

# Sidebar
with st.sidebar:
    st.header("Navigation 📋")
    st.write("Welcome to my interactive app!")
    st.write("---")
    st.info("This app demonstrates various Streamlit features including user input, data visualization, and recommendations.")
    
    # Show user statistics
    st.write("---")
    st.subheader("📈 User Statistics")
    user_data = load_user_data()
    if not user_data.empty:
        st.metric("Total Users", len(user_data))
        if 'age' in user_data.columns:
            avg_age = user_data['age'].mean()
            st.metric("Average Age", f"{avg_age:.1f}")
        if 'favorite_genre' in user_data.columns:
            top_genre = user_data['favorite_genre'].mode()[0] if not user_data['favorite_genre'].empty else "N/A"
            st.metric("Most Popular Genre", top_genre)
    else:
        st.info("No user data yet!")

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

# Section 3: Movie Recommender with Data Collection
st.header("🎬 Movie Recommender")
st.markdown("Get personalized movie recommendations based on your favorite genre!")

# User registration form
with st.form("user_form"):
    st.subheader("📝 Tell us about yourself")
    form_col1, form_col2, form_col3 = st.columns([2, 1, 2])
    
    with form_col1:
        form_name = st.text_input("Your Name", placeholder="Enter your name")
    
    with form_col2:
        form_age = st.number_input("Age", min_value=1, max_value=120, value=25)
    
    with form_col3:
        form_genre = st.selectbox(
            "Favorite Genre", 
            ["Sci-Fi", "Animation", "Action", "Comedy"],
            help="Select your favorite movie genre"
        )
    
    submitted = st.form_submit_button("Get Recommendations & Save", type="primary")
    
    if submitted:
        if form_name.strip():
            # Save the data
            if save_user_data(form_name, form_age, form_genre):
                st.success(f"✅ Thanks {form_name}! Your preferences have been saved.")
                
                # Extended movie database
                movies = {
                    "Sci-Fi": ["🎬 Inception", "🎬 The Matrix", "🎬 Interstellar", "🎬 Blade Runner"],
                    "Animation": ["🎬 Toy Story", "🎬 The Lion King", "🎬 Finding Nemo", "🎬 Spirited Away"],
                    "Action": ["🎬 Die Hard", "🎬 Mad Max", "🎬 John Wick", "🎬 The Dark Knight"],
                    "Comedy": ["🎬 The Hangover", "🎬 Superbad", "🎬 Groundhog Day", "🎬 Step Brothers"]
                }
                
                st.markdown(f"### 🎥 Recommended {form_genre} movies for you:")
                cols = st.columns(2)
                for idx, movie in enumerate(movies[form_genre]):
                    with cols[idx % 2]:
                        st.info(movie)
                
                # Reload to update statistics in sidebar
                st.rerun()
        else:
            st.error("⚠️ Please enter your name!")

st.write("---")

# Section 4: View Collected Data (Admin View)
with st.expander("🔍 View All Collected Data (Admin)"):
    user_data = load_user_data()
    if not user_data.empty:
        st.subheader(f"📊 Total Submissions: {len(user_data)}")
        st.dataframe(user_data, use_container_width=True)
        
        # Analytics
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("**Age Distribution**")
            if 'age' in user_data.columns:
                st.bar_chart(user_data['age'].value_counts().sort_index())
        
        with col_b:
            st.markdown("**Genre Preferences**")
            if 'favorite_genre' in user_data.columns:
                genre_counts = user_data['favorite_genre'].value_counts()
                st.bar_chart(genre_counts)
        
        with col_c:
            st.markdown("**Statistics**")
            if 'age' in user_data.columns:
                st.write(f"**Youngest:** {user_data['age'].min()} years")
                st.write(f"**Oldest:** {user_data['age'].max()} years")
                st.write(f"**Average:** {user_data['age'].mean():.1f} years")
        
        # Download button
        csv = user_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv,
            file_name=f"user_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No data collected yet. Be the first to submit!")
    
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