import streamlit as st
from PIL import Image
import os
import google.generativeai as genai
import json
import requests
from io import BytesIO

st.set_page_config(layout="wide")

st.title("Piculator")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Metadata Creator", "Image Creator"])

# File Browser
st.sidebar.header("File Browser")

@st.cache_data
def get_files(path):
    files = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                files.append(os.path.join(dirpath, filename))
    return files

root_path = st.sidebar.text_input("Enter a directory to browse", "C:\\")

if os.path.isdir(root_path):
    all_files = get_files(root_path)
    selected_file = st.sidebar.selectbox("Select a file", all_files)

    if selected_file:
        st.sidebar.image(selected_file, use_column_width=True)

        if app_mode == "Metadata Creator":
            st.header("Metadata Creator")
            col1, col2 = st.columns(2)
            with col1:
                st.image(selected_file, use_column_width=True)
            with col2:
                st.header("Metadata")
                if st.button("Extract Metadata"):
                    with st.spinner("Extracting metadata..."):
                        try:
                            genai.configure(api_key="AIzaSyBxVyDDVN7dftzNav-bRli9ikaSiJ9FcoA")
                            model = genai.GenerativeModel('gemini-pro-vision')
                            img = Image.open(selected_file)
                            response = model.generate_content(["Extract metadata from this image.", img], stream=True)
                            response.resolve()
                            st.json(response.text)
                        except Exception as e:
                            st.error(f"Error: {e}")

        elif app_mode == "Image Creator":
            st.header("Image Creator")
            col1, col2 = st.columns([2,1])
            with col1:
                st.image(selected_file, use_column_width=True)
            with col2:
                prompt = st.text_area("Enter your prompt")
                if st.button("Generate Images"):
                    with st.spinner("Generating images..."):
                        # Placeholder for image generation
                        st.image("https://picsum.photos/400/400", caption="Version 1")
                        st.image("https://picsum.photos/400/400", caption="Version 2")
                        st.image("https://picsum.photos/400/400", caption="Version 3")
else:
    st.sidebar.error("Invalid directory path")