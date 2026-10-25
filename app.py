import os
import streamlit as st
from PIL import Image
from google import genai
from google.genai import types

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Gemini Vision Test", page_icon="🍽️")

st.title("🍽️ Gemini Vision Test")

# -----------------------------
# Load API Key
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found!")
    st.stop()

st.success("✅ API Key Loaded")

# -----------------------------
# Create Gemini Client
# -----------------------------
client = genai.Client(api_key=API_KEY)

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Image"):

        try:

            # Convert image to bytes
            image_bytes = uploaded_file.getvalue()

            # Detect MIME type
            mime_type = uploaded_file.type

            image_part = types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            )

            response = client.models.generate_content(

                model="gemini-2.0-flash",

                contents=[
                    image_part,
                    "Identify all foods in this image. Respond in one short paragraph."
                ]

            )

            st.success("✅ Gemini Response")

            st.write(response.text)

        except Exception as e:

            st.error("❌ Error")
  
