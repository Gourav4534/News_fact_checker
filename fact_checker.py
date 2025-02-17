import gradio as gr
import google.generativeai as genai
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Gemini API (for generating AI content)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Retrieve API key from environment
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Set up Google Custom Search API (for live, real-time search)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Retrieve API key from environment
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')  # Retrieve Search Engine ID from environment

# Function to search the web using Google Custom Search API
def search_web(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    results = response.json()
    # Filter out irrelevant results and prioritize news sources for real-time validation
    links = [item['link'] for item in results.get('items', []) if 'news' in item['link'] or 'article' in item['link']]
    return links

# Function to fact-check using Gemini API (refined prompt for real-time data analysis)
def fact_check(text):
    prompt = f"Perform a fact-check on the following statement by verifying it with up-to-date sources and context: {text}. Provide a detailed analysis with references and a confidence rating."
    response = model.generate_content(prompt)
    return response.text

# Main function to process input
def process_input(input_data):
    # Fact-check the extracted text
    analysis = fact_check(input_data)

    # Search the web for verification and more real-time information
    search_results = search_web(input_data)

    return analysis, search_results

# Gradio Interface
def gradio_interface(input_data):
    analysis, search_results = process_input(input_data)
    output = f"Analysis:\n{analysis}\n\nSource Links:\n" + "\n".join(search_results[:5])  # Show top 5 relevant links
    return output

# Create Gradio App
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(label="Text Input"),
    outputs=gr.Textbox(label="Fact-Check Results"),
    title="AI News Checker",
    description="Enter text to fact-check news using Gemini API and real-time web search."
)

# Launch the app
iface.launch()
