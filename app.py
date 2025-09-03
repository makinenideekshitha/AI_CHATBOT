from flask import Flask, render_template, request, jsonify
import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Check if API key is loaded
api_key = os.getenv("GOOGLE_API_KEY")
print("API Key Loaded?", bool(api_key))

# Configure Gemini API
if api_key:
    genai.configure(api_key=api_key)
else:
    print("ERROR: Google API key not found. Check your .env file!")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(user_message)
        text = response.text

        # --- Full Markdown cleanup ---
        # Remove bold **text**
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        # Remove italic *text* (single asterisk)
        text = re.sub(r"\*(.*?)\*", r"\1", text)
        # Remove italic _text_ (underscore style)
        text = re.sub(r"\_(.*?)\_", r"\1", text)
        # Remove headings (#, ##, ###)
        text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
        # Remove bullet points * or -
        text = re.sub(r"^\s*[\*\-]\s*", "", text, flags=re.MULTILINE)
        # Remove numbered lists like 1. 2. etc.
        text = re.sub(r"^\s*\d+\.\s*", "", text, flags=re.MULTILINE)
        # Replace multiple newlines with space
        text = re.sub(r"\n+", " ", text)
        # Replace multiple spaces with single space
        text = re.sub(r"\s+", " ", text)
        # Strip leading/trailing spaces
        clean_text = text.strip()

        return jsonify({"reply": clean_text})

    except Exception as e:
        print("Error from Gemini API:", e)
        return jsonify({"reply": f"Error: Could not get AI response. ({e})"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
