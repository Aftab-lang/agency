import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS  # For text-to-speech
import tempfile  # For temporary file handling

load_dotenv()

# Force a complete reset of the session state at startup
if not st.session_state.get('initialized', False):
    # Clear all session state
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.initialized = True

st.set_page_config(
    page_title="Software Agency Chatbot",
    page_icon=":robot_face:",
    layout="wide",
)

# Initialize Gemini-Pro with temperature 0
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro', 
    generation_config={
        'temperature': 0,
        'top_p': 1,
        'top_k': 1,
        'max_output_tokens': 100,
    })

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Initialize chat without sending initial prompt
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.initial_prompt_sent = False

# Display Form Title
st.title("Software Agency Chatbot")

# Display chat messages from history
displayed_messages = st.session_state.chat.history[2:] if len(st.session_state.chat.history) > 2 else st.session_state.chat.history
for message in displayed_messages:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("Hello! How can I assist you today?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # If this is the first message, send the initial prompt first
    if not st.session_state.get('initial_prompt_sent', False):
        initial_prompt = """You are a virtual assistant for  a software development company. Your role is strictly limited to:

1. ONLY discuss Codsmine's services: Mobile App Development
Website Development
Software Development
Graphic Designing
eCommerce Store
Digital Marketing
Content Writing
Online Classes
UI/ UX Design
Blog Writing
SEO
2. NEVER provide information about any other topics
3. Keep responses brief (2 lines maximum)
4. Always suggest scheduling a meeting to discuss project details and suggest discussing via mail or phone and then provide the phone number
5. Identify yourself as Codsmine's virtual assistant if asked
6. Ask for phone number, email, name, and time of meeting when the user is present, and then schedule a meeting. Let them know these are compulsory to schedule a meeting; after confirming, tell them you have sent an email to the provided email.
7. If any question is not related to Codsmine's services, respond with: "I can only assist with inquiries about Codsmine's software development services."

Contact info:
64A Other Road, Redditch, B98 8DT, United Kingdom.

info@codsmine.com

+447572438281
https://codsmine.com/
Remember: Stay strictly within these boundaries and maintain professional, concise responses."""
        st.session_state.chat.send_message(initial_prompt, stream=False)
        st.session_state.initial_prompt_sent = True
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last response
    with st.chat_message("assistant"):
        st.markdown(response.text)
        
        # Convert the response to speech
        tts = gTTS(response.text, lang="en")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        
        # Play the audio in Streamlit
        st.audio(temp_file.name, format="audio/mp3")
