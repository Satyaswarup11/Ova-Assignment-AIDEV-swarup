# Gemini LLM Application

This is an advanced AI-powered application built using Streamlit that leverages the Gemini Pro language model. The application combines various functionalities, including natural language processing, image understanding, and speech recognition.

## Features

1. Chat with Gemini Pro:
    - Utilizes the Gemini Pro language model to provide detailed responses to user queries.
    - Maintains a chat history displayed on the page.
2. Image Understanding:
    - Allows users to upload an image and receive responses based on the content of the image.
    - Uses the Gemini 1.0 Pro Vision model for image-related inquiries.
3. PDF Information Extraction:
    - Enables users to upload PDF files and extract information from the content.
    - Utilizes natural language processing to understand the text in PDFs.
4. Speech Recognition and Synthesis:
    - Incorporates speech recognition to understand user input via voice.
    - Provides responses through text-to-speech synthesis.
5. Music Playback:
    - Includes a feature to play music by recognizing the command "play music."
    
## Installation:

1. Clone Repository:
   ```bash
   git clone https://github.com/Satyaswarup11/Ova-Assignment-AIDEV-swarup.git
   ```

2. Create Virtual Environment (Optional): For project isolation and dependency management, consider creating a virtual environment using tools like venv or conda. <br>
   For windows :
   ```bash
   python3 -m venv myenv
   ```
   Activate it :
   ```bash
   cd myenv
   Scripts/Activate
   ```
4. Install Dependencies: Navigate to the project directory and run to install required dependencies :
   ```bash
   pip install -r requirements.txt 
   ```
## Usage:

- Go to Google AI studio and get gemini API key. Instead of publicily sharing your key, create a file named .env in the root directory and Add the following line in the file:
  ```
  GOOGLE_API_KEY=YOUR_API_KEY
  ```
- Run the Application: Execute streamlit run in your terminal to launch the Streamlit app interface.
  ```bash
  streamlit run Advanced_Ai.py
  ```
- Chatting with Gemini Pro:
   - Enter your text in the "Input" field and click "Ask anything."
   - View responses in the chat history section.
- Image Understanding:
   - Upload an image using the "Tell me about the image" button.
   - Receive responses based on the image content.
- PDF Information Extraction:
   - Upload PDF files using the "Get pdf info" button.
   - Extracted information will be displayed.
- Speech Recognition:
   - Click the "Speak" button in the sidebar to provide input via voice.
   - Responses will be displayed in the chat history.
- Music Playback:
   - Say "play music" to initiate music playback.

### Summary of the Mechanisms
- Interact with the AI: Engage in text-based conversations through the provided input field.
- Audio Interaction: Click the "Speak" button to activate speech recognition and interact with the AI using your voice.
- File Uploads: Utilize the upload functionalities to process images (JPG, JPEG, PNG) and can upload multiple pdfs and process at the same time.
- Function Calling Mechanism: Users can direclty play music of the specific path provided in the code from the streamlit application

