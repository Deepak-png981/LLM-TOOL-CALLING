from pathlib import Path
from typing import Literal
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Config:
    SUPPORTED_IMAGE_TYPES = [".jpg", ".jpeg", ".png", ".bmp"]
    SUPPORTED_AUDIO_TYPES = [".mp3", ".wav", ".m4a"]
    SUPPORTED_VIDEO_TYPES = [".mp4", ".avi", ".mov"]
    
    TEMP_DIR = Path("temp")
    OUTPUT_DIR = Path("output")
    
    TEMP_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
