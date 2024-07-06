# S&P 500 Trading Decision and Insights App

This project is an AI-powered application designed to provide real-time trading decisions and insights for S&P 500 stocks. It leverages Pathway’s LLM (Large Language Model) App features to build a robust data pipeline in Python, integrating OpenAI's Embeddings and Chat Completion APIs for generating AI assistant responses.

## Features

- **Real-time Stock Decisions**: Offers daily buy, sell, or hold predictions for S&P 500 stocks based on machine learning classifiers.
- **Interactive UI**: Utilizes Streamlit for a user-friendly interface to interact with the app and view stock insights.
- **Data Reusability**: Implements data and code reusability, supporting various data formats and sources including JSONLines and CSV.
- **Extendable Data Sources**: Integrates seamlessly with external APIs, databases (e.g., PostgreSQL, MySQL), and streaming platforms (e.g., Kafka, Redpanda, Debezium).

## Core Functionality

The application preprocesses historical OHLCV (Open, High, Low, Close, Volume) data for S&P 500 stocks, computes technical indicators, trains multiple classifiers, and generates predictions. Predictions are compiled into a CSV file and further processed into JSONLines format, incorporating detailed information about each indicator's impact on the trading decision.

## Usage

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YourUsername/SP500-Trading-App.git
   cd SP500-Trading-App
   ```

2. **Set Environment Variables:**

   Create a `.env` file in the project root directory with your configuration:

   ```bash
   OPENAI_API_TOKEN=your_openai_api_key
   HOST=0.0.0.0
   PORT=8080
   EMBEDDER_LOCATOR=text-embedding-ada-002
   EMBEDDING_DIMENSION=1536
   MODEL_LOCATOR=gpt-3.5-turbo
   MAX_TOKENS=200
   TEMPERATURE=0.0
   ```

3. **Install Dependencies:**

   Install the required Python packages:

   ```bash
   pip install --upgrade -r requirements.txt
   ```

4. **Run the Application:**

   Start the application:

   ```bash
   python main.py
   ```

   Ensure the application is running successfully by accessing `http://localhost:8080` in your web browser.

### Data Processing Workflow

1. **Data Preparation:**

   - **Download S&P 500 Data:** Retrieves the latest S&P 500 company list from Wikipedia and adjusts ticker symbols for compatibility with Yahoo Finance.
   - **Compute Indicators:** Calculates essential technical indicators (e.g., SMA, MACD, RSI) using historical stock data fetched via yfinance library.

2. **Model Prediction:**

   - **Generate Predictions:** Applies machine learning classifiers to predict daily stock decisions (buy, sell, hold) based on computed indicators.
   - **Compile Predictions:** Aggregates predictions into a comprehensive dataset for further analysis and reporting.

3. **Output Generation:**

   - **Export to CSV:** Saves the aggregated predictions into a CSV file (`nifty_50_predictions.csv`).
   - **Convert to JSONLines:** Transforms the CSV file into a structured JSONLines format (`stock_predict_total.jsonl`), incorporating detailed indicator information.

4. **Integration with LLM App:**

   - **Embedding Process:** Utilizes OpenAI's Embeddings API to embed the JSONLines data, enhancing data retrieval and analysis capabilities.
   - **Combine Data:** Integrates the embedded data with additional indicator information into a consolidated JSONLines file (`stock_predict_total.jsonl`).

### Future Enhancements

- **Expandable Data Sources:** Incorporate additional external APIs and data streams for broader market coverage.
- **Predictive Modeling:** Integrate future price prediction models and Risk Assessment & Growth can ensure more efficient results.
- **UI and Functionality Improvements:** Enhance user interface capabilities and provide more in-depth financial insights for queried stocks.
- **Scalability:** Extend the application's usability to cover a wider range of stocks beyond the S&P 500 index.

## Acknowledgments

This project is based on the original work found at [Original Repository Link](https://github.com/CodeAceKing382/Stocks-Insight-App). Special thanks to the original authors for their work.

### Contributing

Contributions to enhance and expand the functionality of the application are welcome. Please fork the repository, make your changes, and submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
