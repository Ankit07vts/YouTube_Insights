# VidBot-YouTube-Insights

## Summary
The **VidBot-YouTube-Insights** is a Streamlit-based web application that allows users to fetch, summarize, and interact with transcripts from YouTube videos. It integrates with OpenAI's GPT-3.5 to generate AI-based summaries and answer questions based on video content. This project uses LangChain for text splitting and vector-based operations, enabling sophisticated features like similarity searches and interactive question-answering.

## Introduction
This project is designed to provide a user-friendly interface for summarizing and interacting with YouTube video content. Users can submit a YouTube video link to get a summarized version of the transcript, ask questions based on the video content, and receive AI-generated responses. The application includes robust error handling, progress indicators, and a modular design for scalability.

## Advantages and Disadvantages
### Advantages
- **AI Integration**: Utilizes OpenAI GPT-3.5, providing advanced text summarization and question-answering capabilities.
- **YouTube Transcript Extraction**: Automatically fetches and processes transcripts from YouTube videos.
- **Interactive and Engaging**: Allows users to ask questions and provides real-time feedback with progress indicators.
- **Scalable Design**: Built with a modular approach, facilitating easy modification and expansion.
- **Robust Error Handling**: Includes fallback mechanisms for smooth operation even under challenging conditions.

### Disadvantages
- **OpenAI Costs**: Interaction with OpenAI's API may incur costs, especially with frequent use.
- **Transcript Limitations**: Some YouTube videos might not have transcripts, limiting functionality.
- **Environment Variables**: Requires proper setup of environment variables for OpenAI integration.

## Requirements
To run this project, ensure you have the following:
- Python 3.7 or later
- Streamlit (latest version)
- OpenAI package
- youtube-transcript-api
- langchain
- dotenv
- FAISS (for vector-based operations)
- PyPDF2 (if additional functionality with PDFs is needed)

Additionally, you will need an OpenAI API key to access GPT-3.5 features. This requires setting up an OpenAI account and obtaining an API key.

## Installation Process
To install and run the VidBot-YouTube-Insights, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/your-project.git
   cd your-project

2. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Configure Environment Variables**:
   Create a .env file in the project directory and add your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

4. **Run the Streamlit App**:
   Launch the Streamlit application:
   ```bash
   streamlit run app.py

5. **Access the App**:
   Once Streamlit is running, open the provided URL in a web browser to access the application.
