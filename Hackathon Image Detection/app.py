from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import time
import re

# Load environment variables
load_dotenv()

# Configure the generative AI model
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API Key not found in environment variables.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Directory to store uploaded images
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to get a response from the Gemini API
def get_gemini_response(input_text, image):
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif image:
        response = model.generate_content(image)
    elif input_text:
        response = model.generate_content([input_text])
    else:
        return "No input provided."
    
    if response and response.parts:
        return response.parts[0].text
    else:
        return "No valid response returned by the model."

# Function to display text in a streaming manner by chunks
def stream_response(response_text, chunk_size=14):
    placeholder = st.empty()
    words = response_text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    
    text = ""
    for chunk in chunks:
        for letter in chunk:
            text += letter
            placeholder.text(text)
            time.sleep(0.01)  # Adjust the speed of letter streaming here
        text += ""
        placeholder.text(text)
        time.sleep(0.5)  # Adjust the speed of chunk streaming here

# Sanitize filename
def sanitize_filename(filename: str) -> str:
    """
    Sanitize the filename to remove or replace invalid characters.
    """
    sanitized = re.sub(r'[<>:"/\\|?*\n]', '-', filename)
    sanitized = re.sub(r'-', ' ', sanitized)
    return sanitized

# Combined function to save file, get response, and rename file
def process_and_rename_file(uploaded_file):
    # Save the file
    original_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(original_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Open the image directly from the file-like object
    image = Image.open(uploaded_file)  # Use the file-like object directly
    
    # Generate description
    with st.spinner('Generating response...'):
        description = get_gemini_response(
                                        '''
                                        Give me all the details I would need to know for finding this device. \n
                                        Include the brand, model, and any other relevant information. Give it \n
                                        in single keywords. If there is text, do NOT extract it. Only describe \n
                                        the object in the image. Give different keywords for the object.
                                        ''',
                                        image
                                        )
    
    # Sanitize and create new filename based on response
    sanitized_description = sanitize_filename(description)
    new_filename = f"{sanitized_description}.jpg"
    new_path = os.path.join(UPLOAD_DIR, new_filename)
    
    # Rename the file
    if new_path != "No valid response returned by the model..jpg":
        os.rename(original_path, new_path)
    
    return new_path, description

# Function to save user information
def save_user_info(image_path, user_info):
    info_path = os.path.splitext(image_path)[0] + '.txt'
    with open(info_path, 'w') as f:
        f.write(user_info)

# Main page for image upload and description
def upload_page():
    st.title("🖼️ Upload the Image of the Item Found")
    st.write("Upload an image of the item you have found, and we will provide a description based on the visual content.")
    
    # Input for user information
    user_info = st.text_input("Tell us about yourself (optional):", key="user_info")
    
    uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"], key="upload_image")
    
    if uploaded_file:
        new_path, description = process_and_rename_file(uploaded_file)
        # Save user info with the image
        save_user_info(new_path, user_info)
        st.image(new_path, caption='Uploaded Image', use_column_width=True)
        st.write("### Description:")
        st.write(description)

# Search page
def search_page():
    st.title("🔍 Search for Images")
    st.write("Search for images based on their filename or description.")

    search_query = st.text_input("Search by Keywords of item", key="search_query")
    
    if search_query:
        display_search_results(search_query)


def display_search_results(query):
    # Normalize and tokenize the query
    query_tokens = set(re.split(r'\s+', query.lower()))
    
    # List all images
    image_files = list_images()
    
    results = []
    for image_file in image_files:
        # Normalize the image file name
        file_name = os.path.splitext(image_file)[0].lower()
        
        # Tokenize the file name
        file_tokens = set(re.split(r'\s+', file_name))
        
        # Check if all query tokens are in the file tokens
        if query_tokens.issubset(file_tokens):
            results.append(image_file)
    
    # Display results
    if results:
        st.write(f"Found {len(results)} result(s):")
        for image_file in results:
            image_path = os.path.join(UPLOAD_DIR, image_file)
            info_path = os.path.splitext(image_path)[0] + '.txt'
            user_info = ""
            if os.path.exists(info_path):
                with open(info_path, 'r') as f:
                    user_info = f.read()
            st.image(image_path, caption=image_file, use_column_width=True)
            if user_info:
                st.write("### Information about the finder:")
                st.write(user_info)
    else:
        st.write("No results found.")

def list_images():
    image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.jpg', '.jpeg', '.png'))]
    return image_files


# Main function to display pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a Page", ["Upload Image", "Search Images"], key="page_selector")
    
    if page == "Upload Image":
        upload_page()
    elif page == "Search Images":
        search_page()

if __name__ == "__main__":
    main()
