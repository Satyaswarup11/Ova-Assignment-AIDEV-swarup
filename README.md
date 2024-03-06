## Advanced AI Application with Text-to-Text, Audio-to-Audio

### Description:

This project showcases a remarkable AI application featuring comprehensive functionalities:

- Text-to-Text and Audio-to-Audio Communication: Seamlessly engage in both text-based and speech-driven interactions through intuitive input methods.
- Image and Document Processing: Enhance versatility by supporting a wider range of file types, including images (JPG, JPEG, PNG), PDFs, Excel files, and Word documents, for comprehensive information extraction and analysis.
- Voice control: Leverage convenient voice control by simply speaking and automatically triggering responses, making interaction more natural and hands-free.
- Function Calling: Automate tasks seamlessly with the capability to schedule calendar events, send emails, and set reminders directly within the application. Added 'play music' functionilaity in the application
- Human-like Communication: Strives to replicate natural human conversation patterns, creating a more engaging and intuitive user experience.

### Installation:

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

 ### Usage:
- Go to Google AI studio and get gemini API key. Instead of publicily sharing your key, create a file named .env in the root directory and Add the following line in the file:
  ```
  GOOGLE_API_KEY=YOUR_API_KEY
  ```
- Run the Application: Execute streamlit run in your terminal to launch the Streamlit app interface.
  ```bash
  streamlit run Advanced_Ai.py
  ```
- Interact with the AI: Engage in text-based conversations through the provided input field.
- Audio Interaction: Click the "Speak" button to activate speech recognition and interact with the AI using your voice.
- File Uploads: Utilize the upload functionalities to process images (JPG, JPEG, PNG) and can upload multiple pdfs and process at the same time.
- Function Calling Mechanism: Users can direclty play music of the specific path provided in the code from the streamlit application

