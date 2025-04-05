from dotenv import load_dotenv

load_dotenv()

import streamlit as st # for the web app
import os
from  PIL import Image # for image processing
import pdf2image # for pdf to image conversion
import google.generativeai as genai # for AI model

genai.configure(api_key=os.getenv("API_KEY")) # Set the API key for the AI model

def gemini 