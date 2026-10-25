import os
import streamlit as st
from PIL import Image
from google import genai

st.title("Gemini Vision Test")

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg","jpeg","png"]
)

if uploaded:

    image = Image.open(uploaded)

    st.image(image)

    if st.button("Analyze"):

        try:

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=[
                    image,
                    "What food is shown in this image? Answer in one sentence."
                ]

            )

            st.success(response.text)

        except Exception as e:

            st.exception(e)
