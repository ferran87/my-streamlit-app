# My First Streamlit App 🚀

A simple, interactive Streamlit web application featuring user input, data visualization, and a movie recommender.

## Features

- **Interactive Greeting**: Enter your name and get a personalized greeting
- **Age Slider**: Interactive slider to input your age
- **Data Visualization**: Displays a random line chart
- **Movie Recommender**: Get movie recommendations based on genre (Sci-Fi or Animation)

## Live Demo

🌐 [View the live app here](#) _(Link will be available after deployment)_

## Local Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd MCP
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Dependencies

- streamlit >= 1.30.0
- pandas >= 2.0.0
- numpy >= 1.24.0

## Deployment

This app is deployed on Streamlit Community Cloud. Any changes pushed to the main branch will automatically update the live app.

## Project Structure

```
MCP/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Usage

1. **Enter Your Name**: Type your name in the text input field and click "Say hello"
2. **Adjust Age Slider**: Move the slider to select your age
3. **View Chart**: See the automatically generated random data visualization
4. **Get Movie Recommendations**: Select a genre to get movie suggestions

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available under the MIT License.

