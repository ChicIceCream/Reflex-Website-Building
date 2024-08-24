# state.py
import os

from dotenv import load_dotenv
load_dotenv()
import reflex as rx
# from reflex.gemini import GeminiClient
import pathlib
import textwrap

import google.generativeai as genai

# Checking if the API key is set properly
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise Exception("Please set GOOGLE_API_KEY environment variable.")
else:
    print(f"API Key Loaded: {api_key[:5]}...")  # Print the first few characters for verification

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

class TutorialState(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def clear_chat(chat_history):
        chat_history = []
    
    def answer(self):
        response = model.generate_content(self.question)


        # Add to the answer as the chatbot responds.
        answer = response.text
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield
