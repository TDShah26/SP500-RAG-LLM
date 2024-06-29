import os
import random
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Set page configuration
st.set_page_config(
    page_title="S&P 500 Trade Decision and Insights",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Streamlit UI elements
st.title("📈 S&P 500 Trade Decision and Insights")
st.markdown(
    """
    ## How to use:
    
    Enter a question about price-action decision for any stock in the S&P 500 or as a whole,
    and the AI will provide a decision along with justification and explanation through financial analysis.
    
    ---
    """
)

question = st.text_input(
    "Enter your question here (Please mention the stock by ticker symbol):",
    placeholder="E.g., What will be my price-action decision for AAPL stock today? Find best stocks to buy today.",
)

# Handle the query submission
if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.markdown("---")
        st.subheader("Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to obtain insights. Status code: {response.status_code}")

# Random investment quotes
quotes = [
    {
        "author": "Warren Buffett",
        "quote": "The stock market is a device for transferring money from the impatient to the patient."
    },
    {
        "author": "Peter Lynch",
        "quote": "Know what you own, and know why you own it."
    },
    {
        "author": "Benjamin Graham",
        "quote": "In the short run, the market is a voting machine, but in the long run, it is a weighing machine."
    },
    {
        "author": "John Templeton",
        "quote": "The time of maximum pessimism is the best time to buy, and the time of maximum optimism is the best time to sell."
    },
    {
        "author": "Charlie Munger",
        "quote": "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price."
    }
]

random_quote = random.choice(quotes)

# Display random quote with scroll bar if needed
st.markdown(
    f'<div style="max-height: 200px; overflow-y: auto;">'
    f'### "{random_quote["quote"]}"'
    f'<br>- *{random_quote["author"]}*'
    f'</div>',
    unsafe_allow_html=True
)

# Optional: Add background color and other styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: #1a1a1a;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    .css-1bq9g1x.e1b8pzkj0 {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
