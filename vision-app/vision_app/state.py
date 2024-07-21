import asyncio
import reflex as rx
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import shutil

# Load environment variables from the .env file
load_dotenv()

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
    image_path: str = ""

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
        question = form_data.get("question", "")
        image_file = form_data.get("image", None)
        
        if question:
            async for value in self.gemini_process_question(question):
                yield value
        elif image_file:
            # Save the uploaded file to a temporary location
            temp_file_path = "uploaded_image.jpg"  # You can choose a more dynamic name if needed
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(image_file)
            
            # Process the image
            async for value in self.process_image(temp_file_path):
                yield value

    async def gemini_process_question(self, question: str):
        """Get the response from the Gemini API with streaming effect."""
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

        # Simulate streaming
        full_text = ""
        for chunk in response:
            if chunk.text:
                full_text += chunk.text
                # Break the text into smaller chunks to simulate streaming
                for i in range(0, len(full_text), 14):  # Chunk size of 14 characters
                    self.chats[self.current_chat][-1].answer = full_text[:i]
                    self.chats = self.chats
                    await asyncio.sleep(0.01)  # Adjust the speed of letter streaming here
                self.chats[self.current_chat][-1].answer = full_text
                self.chats = self.chats
                await asyncio.sleep(0.5)  # Adjust the speed of chunk streaming here

        self.processing = False

    async def process_image(self, image_path: str):
        """Get the description of the image."""
        qa = QA(question="Describe this image", answer="")
        self.chats[self.current_chat].append(qa)
        
        self.processing = True
        yield

        # Open the image using Pillow
        try:
            image = Image.open(image_path)
            description = f"Image format: {image.format}, Size: {image.size}, Mode: {image.mode}"
        except Exception as e:
            description = f"Error processing image: {str(e)}"

        self.chats[self.current_chat][-1].answer = description
        self.chats = self.chats  # Trigger a state update
        
        self.processing = False
