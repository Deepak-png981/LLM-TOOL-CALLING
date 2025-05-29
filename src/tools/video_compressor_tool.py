import ffmpeg
from pathlib import Path
from loguru import logger
from .base import BaseTool
from ..config import Config

class VideoCompressorTool(BaseTool):
    name: str = "VideoCompressor"
    description: str = "Compresses video files using ffmpeg"
    
    async def _arun(self, input_data: str) -> str:
        try:
            input_path = Path(input_data)
            output_path = Config.OUTPUT_DIR / f"compressed_{input_path.name}"
            
            stream = ffmpeg.input(str(input_path))
            stream = ffmpeg.output(
                stream,
                str(output_path),
                vcodec='libx264',
                acodec='aac',
                preset='medium',
                crf=23,  # Balanced quality (0-51, lower is better)
                audio_bitrate='128k'
            )
            
            ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
            
            logger.info(f"Successfully compressed video to {output_path}")
            return str(output_path)
            
        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {str(e.stderr.decode())}")
            raise
        except Exception as e:
            logger.error(f"Error in video compression: {str(e)}")
            raise