# AI_CHATBOT 

# AI Chatbot with Google Gemini API

This is a **web-based AI Chatbot** built using **Python Flask** and **Google Gemini Generative AI API**. The chatbot provides real-time responses to user queries using advanced language models.

---

## Features

- Chat with a Gemini-powered AI model in real-time
- Clean, responsive frontend using HTML, CSS, JavaScript, and Bootstrap
- Flask backend to handle API requests and manage chat sessions
- Environment-based API key management to keep secrets safe
- Modular project structure for easy maintenance and expansion

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Python Flask  
- **AI:** Google Generative AI (Gemini LLM)  
- **Environment management:** Python `.venv` and `.env` for API keys  

---

## Prerequisites

- Python 3.10 or higher  
- pip package manager  
- Google API key for Gemini API  

## How to Run AI Chatbot ?

Step 1: Clone the Repository

Go to your terminal and run: git clone https://github.com/makinenideekshitha/AI_CHATBOT.git

Change into the project folder: cd AI_CHATBOT

Step 2: Create a Virtual Environment

Run: python3 -m venv .venv to create a virtual environment.

Activate it:

On macOS/Linux: source .venv/bin/activate

On Windows: .venv\Scripts\activate

Step 3: Install Dependencies

Run: pip install -r requirements.txt

Step 4: Create a .env File

In the root folder of your project, create a file named .env.

Add your Google API key like this: GOOGLE_API_KEY=your_api_key_here

Step 5: Run the Chatbot

Run: python app.py

Open your browser and go to local host:8000 to start chatting with the AI.




