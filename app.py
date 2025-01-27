import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, CLIPProcessor, CLIPModel, DetrImageProcessor, DetrForObjectDetection
import faiss
import numpy as np
from dotenv import load_dotenv
import os
import google.generativeai as genai

