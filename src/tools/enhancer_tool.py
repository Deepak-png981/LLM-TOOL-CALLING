import cv2
import numpy as np
from pathlib import Path
from loguru import logger
from .base import BaseTool
from ..config import Config

class EnhancerTool(BaseTool):
    name: str = "Enhancer"
    description: str = "Enhances image quality using OpenCV"
    
    async def _arun(self, input_data: str) -> str:
        try:
            input_path = Path(input_data)
            output_path = Config.OUTPUT_DIR / f"enhanced_{input_path.name}"
            
            # Read image
            img = cv2.imread(str(input_path))
            if img is None:
                raise ValueError(f"Could not read image at {input_path}")
            
            # Convert to LAB color space
            lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            
            # Apply CLAHE to L channel
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            cl = clahe.apply(l)
            
            # Merge channels
            enhanced_lab = cv2.merge((cl, a, b))
            
            # Convert back to BGR
            enhanced_img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
            
            # Apply subtle sharpening
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]])
            enhanced_img = cv2.filter2D(enhanced_img, -1, kernel)
            
            # Save the enhanced image
            cv2.imwrite(str(output_path), enhanced_img)
            
            logger.info(f"Successfully enhanced image at {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error in image enhancement: {str(e)}")
            raise