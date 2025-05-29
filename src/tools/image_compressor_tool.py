from PIL import Image
from pathlib import Path
from loguru import logger
from .base import BaseTool
from ..config import Config

class ImageCompressorTool(BaseTool):
    name: str = "ImageCompressor"
    description: str = "Compresses images while maintaining quality"
    
    async def _arun(self, input_data: str) -> str:
        try:
            input_path = Path(input_data)
            output_path = Config.OUTPUT_DIR / f"compressed_{input_path.name}"
            
            with Image.open(input_path) as img:
                # Convert to RGB if image is in RGBA mode
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Calculate new dimensions while maintaining aspect ratio
                max_size = 1920  # Maximum dimension
                ratio = min(max_size / max(img.size[0], img.size[1]), 1.0)
                new_size = tuple(int(dim * ratio) for dim in img.size)
                
                # Resize and save with optimized compression
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                img.save(
                    output_path,
                    quality=85,  # Good balance between quality and size
                    optimize=True
                )
            
            logger.info(f"Successfully compressed image to {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error in image compression: {str(e)}")
            raise