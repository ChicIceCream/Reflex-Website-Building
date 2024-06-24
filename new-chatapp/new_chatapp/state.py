import reflex as rx
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Checking if the API key is set properly
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise Exception("Please set GOOGLE_API_KEY environment variable.")
else:
    print(f"API Key Loaded: {api_key[:5]}...")  # Print the first few characters for verification

# Configure the Gemini API
genai.configure(api_key=api_key)

class QA(rx.Base):
    """A question and answer pair."""
    question: str
    answer: str

DEFAULT_CHATS = {
    "Intros": [],
}

class State(rx.State):
    """The app state."""
    chats: dict[str, list[QA]] = DEFAULT_CHATS
    current_chat = "Intros"
    question: str
    processing: bool = False
    new_chat_name: str = ""

    def create_chat(self):
        """Create a new chat."""
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]

    def set_chat(self, chat_name: str):
        """Set the name of the current chat."""
        self.current_chat = chat_name

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles."""
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        question = form_data["question"]
        if question == "":
            return
        async for value in self.gemini_process_question(question):
            yield value

    async def gemini_process_question(self, question: str):
        """Get the response from the Gemini API."""
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)

        self.processing = True
        yield

        # Create a new session to answer the question
        model = genai.GenerativeModel("gemini-pro")
        
        # Build the conversation history
        conversation = []
        for qa in self.chats[self.current_chat]:
            conversation.append(qa.question)
            if qa.answer:
                conversation.append(qa.answer)

        # Stream the response
        response = model.generate_content(
            conversation + [question],
            generation_config=genai.types.GenerationConfig(
                temperature=0.9,
                top_p=1,
                top_k=1,
                max_output_tokens=2048,
            ),
            stream=True
        )

        for chunk in response:
            if chunk.text:
                self.chats[self.current_chat][-1].answer += chunk.text
                self.chats = self.chats
                yield

        self.processing = False