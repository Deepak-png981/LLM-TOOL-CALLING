import easyocr
from typing import ClassVar
from loguru import logger
from .base import BaseTool

class OCRTool(BaseTool):
    name: str = "OCR"
    description: str = "Extracts text from images using easyocr"
    reader: ClassVar = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if OCRTool.reader is None:
            OCRTool.reader = easyocr.Reader(['en'])  # You can add more languages if needed

    async def _arun(self, input_data: str) -> str:
        try:
            result = OCRTool.reader.readtext(input_data, detail=0)
            text = "\n".join(result)
            logger.info(f"Successfully extracted text from {input_data}")
            return text.strip()
        except Exception as e:
            logger.error(f"Error in OCR processing: {str(e)}")
            raise 