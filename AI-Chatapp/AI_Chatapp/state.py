# state.py
import os

from openai import AsyncOpenAI

import reflex as rx
# from reflex.gemini import GeminiClient
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
# from google.colab import userdata

genai.configure(api_key='AIzaSyCCj_8HHeEXic4AgTCRMm4ELNIndN6MlK8')

model = genai.GenerativeModel('gemini-pro')


class TutorialState(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        response = model.generate_content(self.question)


        # Add to the answer as the chatbot responds.
        answer = response.text
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield
