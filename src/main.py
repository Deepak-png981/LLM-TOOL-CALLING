from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import mimetypes
from loguru import logger

from .graph import MediaProcessingGraph
from .config import Config

app = FastAPI(title="Smart Media Converter")
graph = MediaProcessingGraph()

@app.post("/process")
async def process_media(
    file: UploadFile,
    instruction: str = Form(...)
):
    try:
        file_path = Config.TEMP_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        file_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        
        result = await graph.process_media(
            instruction=instruction,
            file_path=str(file_path),
            file_type=file_type
        )
        
        return JSONResponse(
            content={
                "status": result.get("status", "error"),
                "instruction": instruction,
                "file_type": file_type,
                "result": result.get("result", ""),
                "message": result.get("message", "")
            }
        )
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )
    finally:
        if file_path.exists():
            file_path.unlink()