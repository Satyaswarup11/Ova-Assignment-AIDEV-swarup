import streamlit as st
import os
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
from PIL import Image
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from pydub import AudioSegment
from pydub.playback import play


from dotenv import load_dotenv

load_dotenv() ## loading all the environment variables
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 

# model = genai.GenerativeModel(model_name="gemini-1.0-pro")

chat = model.start_chat(history=[])

def get_gemini_response_text(question):
    
    response=chat.send_message(question)
    return response


def get_gemini_response(input,image,prompt):
    modell = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest")
    response = modell.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    


def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the pdf", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    st.write("Bot: ", response["output_text"])



def speak(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # engine.startLoop(False)
    # if engine._inLoop:
    #     engine.endLoop()
    engine = None


def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.write("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        st.write(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand.")
        return None
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    

def play_music():
    st.write("Playing music...")
    musicPath = "C:/Users/SATYASWARUP/Videos/Music/Harry-Styles-Grapejuice-(HipHopKit.com).mp3"
    os.system(f"start {musicPath}")





##initialize our streamlit app

st.set_page_config(page_title="Advanced AI")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask anything")
submit2=st.button("Tell me about the image")  
submit3=st.button("Get pdf info")  

if submit3 and input:
    user_input(input)


with st.sidebar:
    st.title("Menu:")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            st.success("Done")

user_input_audio=None
st.sidebar.title("Audio Input:")
audio_input_button = st.sidebar.button("Speak")
if audio_input_button:
    user_input_audio = recognize_speech()

# Audio output
# st.sidebar.title("Audio Output:")
# audio_output_button = st.sidebar.button("Speak Response")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
 

input_prompt = """
               You are an expert in understanding images.
               You will receive input images as  &
               you will have to answer questions based on the input image
               """

## If ask or image button is clicked

if submit2:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("According to image..")
    st.write(response)


elif (submit and input) or user_input_audio:
    if user_input_audio:
        if "play music" in user_input_audio.lower():
            play_music()
        else:
            response=get_gemini_response_text(user_input_audio)
            st.session_state['chat_history'].append(("You", user_input_audio))
            response.resolve()
            print(response.text)
            speak(response.text)
            st.session_state['chat_history'].append(("Bot", response.text))
    else:
        response=get_gemini_response_text(input)
        st.session_state['chat_history'].append(("You", input))
        response.resolve()
        st.session_state['chat_history'].append(("Bot", response.text))


    

    






