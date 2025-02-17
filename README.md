# AI News Fact-Checker

An AI-powered tool designed to verify the accuracy of news and statements in real-time. Leveraging the power of Google's **Gemini AI Model** and **Google Custom Search API**, this tool analyzes and fact-checks news claims instantly, providing you with reliable sources for confirmation or refutation.

## Features

- **Text-based Fact-Checking**: Enter a news statement or claim to be verified.
- **AI-Powered Analysis**: Uses the **Gemini AI Model** to analyze the claim and generate detailed fact-checking insights.
- **Real-time Source Verification**: Utilizes the **Google Custom Search API** to fetch the latest news and reliable sources for validation.
- **Instant Results**: Get a comprehensive analysis of the claim, including supporting or refuting evidence.

## Technologies Used

- **Gemini AI Model**: Analyzes the input text to provide in-depth analysis.
- **Google Custom Search API**: Retrieves real-time search results to verify the claim.
- **Gradio**: User-friendly interface for interaction.
- **Python**: Core programming language for implementation.

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- **Google Gemini API** Key
- **Google Custom Search API** Key

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/news-fact-checker.git
   cd news-fact-checker
   
2. **Create a .env file in the project root and add your API keys**:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key
   GOOGLE_API_KEY=your_google_api_key
   SEARCH_ENGINE_ID=your_search_engine_id
   
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the application:**
   ```bash
   python fact_checker.py

Access the fact-checker: After running the application, open your browser and navigate to http://127.0.0.1:7860 to use the tool.



