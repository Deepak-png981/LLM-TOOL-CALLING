import whisper
from loguru import logger
from typing import Any
from .base import BaseTool

class TranscriberTool(BaseTool):
    name: str = "Transcriber"
    description: str = "Transcribes audio/video files to text using Whisper"
    model: Any = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.model = whisper.load_model("base")
        logger.info("Loaded Whisper model")
        
    async def _arun(self, input_data: str) -> str:
        try:
            result = self.model.transcribe(input_data)
            transcription = result["text"]
            logger.info(f"Successfully transcribed {input_data}")
            return transcription.strip()
        except Exception as e:
            logger.error(f"Error in transcription: {str(e)}")
            raise