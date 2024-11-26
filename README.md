# 💻 Software Agency Chatbot 🤖

## Overview 🌟
The **Software Agency Chatbot** is a powerful virtual assistant for Codsmine, designed to handle customer inquiries with precision and professionalism. The chatbot answers questions about Codsmine's services and helps schedule meetings with potential clients. It also features **text-to-speech (TTS)** functionality to enhance user interaction by providing spoken responses.

---

## Key Features ✨

- **Codsmine-Specific Support**:  
  The chatbot is tailored to discuss only Codsmine's services:
  - Mobile App Development 📱
  - Website Development 🌐
  - Software Development 💾
  - Graphic Designing 🎨
  - eCommerce Store 🛒
  - Digital Marketing 📈
  - Content Writing ✍️
  - Online Classes 📚
  - UI/UX Design 🎭
  - Blog Writing 📝
  - SEO 🚀

- **Concise Responses**:  
  Provides brief, professional replies (max two lines).

- **Meeting Scheduling**:  
  Collects user details like phone number, email, name, and meeting time, then confirms the appointment via email.

- **Text-to-Speech (TTS)**:  
  Converts chatbot responses to audio and plays them directly in the app for accessibility.

- **Professional Boundaries**:  
  If asked about unrelated topics, the chatbot responds:  
  *"I can only assist with inquiries about Codsmine's software development services."*

---

## Setup and Installation 🛠️

### Prerequisites:
- **Python** installed
- Streamlit installed (`pip install streamlit`)
- Google Generative AI API key
- Required libraries: `gTTS`, `python-dotenv`

### Installation Steps:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/aftab-lang/software-agency-chatbot.git
   cd software-agency-chatbot
