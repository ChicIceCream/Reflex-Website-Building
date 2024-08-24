import asyncio
import reflex as rx
import google.generativeai as genai
import os
from PIL import Image
import time

class UploadExample(rx.State):
    uploading: bool = False
    progress: int = 0
    total_bytes: int = 0
    uploaded_files: list[str] = []
    file_path: str = ""  # Add this line to store the file path

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / "invoice_input.jpeg"
            
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
            
            self.uploaded_files.append("invoice_input")
            self.file_path = str(outfile)  # Store the file path
            self.total_bytes += len(upload_data)



    def handle_upload_progress(self, progress: dict):
        self.uploading = True
        self.progress = round(progress["progress"] * 100)
        if self.progress >= 100:
            self.uploading = False

    def cancel_upload(self):
        self.uploading = False
        return rx.cancel_upload("upload3")

def upload_form():
    return rx.vstack(
        rx.upload(
            rx.text("Drag and drop files here or click to select files"),
            id="upload3",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
        ),
        rx.vstack(rx.foreach(rx.selected_files("upload3"), rx.text)),
        rx.progress(value=UploadExample.progress, max=100),
        rx.cond(
            ~UploadExample.uploading,
            rx.button(
                "Upload",
                on_click=UploadExample.handle_upload(
                    rx.upload_files(
                        upload_id="upload3",
                        on_upload_progress=UploadExample.handle_upload_progress,
                    ),
                ),
            ),
            rx.button(
                "Cancel",
                on_click=UploadExample.cancel_upload,
            ),
        ),
        align="center",
    )
class ExtractedInfoState(rx.State):
    user_input: str = ""

    def handle_submit(self):
        # This is where you would call another function with self.user_input
        print(f"Submitted: {self.user_input}")
        # For example: self.another_function(self.user_input)

    def set_user_input(self, value: str):
        self.user_input = value

def extracted_info():
    return rx.vstack(
        rx.text("Enter your prompt : "),
        rx.text_area(
            value=ExtractedInfoState.user_input,
            on_change=ExtractedInfoState.set_user_input,
            height="10rem",
            width="400%",
            border_width="2px",
            variant="soft",
            radius="large",
            name="user_input",
            required=True,
            placeholder="e.g -> total amount in json format"
        ),
        rx.button(
            "Submit",
            type="submit",
            on_click=ExtractedInfoState.handle_submit
        ),
        align="center",
    )

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(image, prompt):
    input_prompt = """
    You are an expert in reading invoices. 
    The user has uploaded an invoice image and is asking for help.
    If the user asks any questions about the invoice, read from the image and 
    provide an answer.
    """
    response = model.generate_content([input_prompt, image[0], prompt])
    return response.text

def input_image_details(upload_file):
    if upload_file is not None:
        # Read the file into bytes
        bytes_data = upload_file.getvalue()
        
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

class AppState(rx.State):
    response_text: str = ""
    displayed_text: str = ""
    chunk_size: int = 14

    async def stream_response(self):
        words = self.response_text.split()
        chunks = [" ".join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]

        text = ""
        for chunk in chunks:
            for letter in chunk:
                text += letter
                self.displayed_text = text  # Update the displayed text dynamically
                await asyncio.sleep(0.01)  # Adjust the speed of letter streaming here
            text += "\n\n"
            self.displayed_text = text
            await asyncio.sleep(0.5)  # Adjust the speed of chunk streaming here

def render():
    return rx.fragment(
        rx.text(AppState.displayed_text),
        rx.button("Start Streaming", on_click=AppState.stream_response),
    )

def launch_gemini(invoice, user_input):
    input_prompt = """
        You are an expert in reading invoices. 
        The user has uploaded an invoice image and is asking for help.
        If the user asks any questions about the invoice, read from the image and 
        provide an answer.
        """

    image_data = input_image_details(invoice)
    response = get_gemini_response(input_prompt, image_data, user_input)
    
    render(response)


def index() -> rx.Component:
    return rx.vstack(
        upload_form(),
        rx.grid(
            rx.foreach(
                UploadExample.uploaded_files,
                lambda img: rx.vstack(
                    rx.image(src=rx.get_upload_url(img)),
                    rx.text(img),
                ),
            ),
        ),
        extracted_info(),
        #launch_gemini(UploadExample.uploaded_files, ExtractedInfoState.user_input),
        align="center"
    )

app = rx.App()
app.add_page(index) 