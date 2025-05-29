# Smart Media Converter

A powerful AI-driven media processing platform that combines multiple tools for intelligent media manipulation, analysis, and conversion. Built with LangChain, FastAPI, and OpenAI's GPT models.

## 🚀 Features

### Core Capabilities
- **🔍 OCR (Optical Character Recognition)**: Extract text from images using EasyOCR
- **🎵 Audio Transcription**: Convert speech to text using OpenAI Whisper
- **🎬 Video Compression**: Optimize video files with FFmpeg
- **🖼️ Image Compression**: Reduce image file sizes while maintaining quality
- **✨ Media Enhancement**: Improve image and video quality
- **📝 AI Summarization**: Generate intelligent summaries using LLM

### AI-Powered Processing
- **Natural Language Instructions**: Process media using simple text commands
- **Intelligent Tool Selection**: AI automatically chooses the right tools for your task
- **Context-Aware Processing**: Understands file types and applies appropriate operations
- **Multi-Step Workflows**: Chains multiple operations based on your instructions

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.8+
- **AI Framework**: LangChain, OpenAI GPT-4
- **Media Processing**: 
  - FFmpeg (video/audio)
  - OpenCV (computer vision)
  - Pillow (image processing)
  - EasyOCR (text extraction)
  - OpenAI Whisper (speech recognition)
- **Logging**: Loguru
- **Environment**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- OpenAI API key
- Tesseract OCR (for advanced OCR features)

### System Dependencies

#### Windows
```bash
# Install FFmpeg via chocolatey
choco install ffmpeg

# Install Tesseract
choco install tesseract
```

#### macOS
```bash
# Install FFmpeg via homebrew
brew install ffmpeg

# Install Tesseract
brew install tesseract
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg tesseract-ocr
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langGraph-game
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. **Create necessary directories**
   ```bash
   mkdir temp output
   ```

## 🚀 Quick Start

### Running the Server

```bash
# Start the FastAPI server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- **Interactive API Docs**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## 📖 Usage Examples

### Basic API Usage

#### Extract Text from Image
```bash
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@image.jpg" \
  -F "instruction=Extract all text from this image"
```

#### Transcribe Audio File
```bash
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@audio.mp3" \
  -F "instruction=Transcribe this audio file to text"
```

#### Compress Video
```bash
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@video.mp4" \
  -F "instruction=Compress this video to reduce file size"
```

#### Complex Multi-Step Processing
```bash
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.jpg" \
  -F "instruction=Extract text from this document image and then summarize the main points"
```

### Python Client Example

```python
import requests

def process_media(file_path, instruction):
    url = "http://localhost:8000/process"
    
    with open(file_path, 'rb') as file:
        files = {'file': file}
        data = {'instruction': instruction}
        
        response = requests.post(url, files=files, data=data)
        return response.json()

# Example usage
result = process_media(
    "path/to/your/image.jpg", 
    "Extract text and enhance image quality"
)
print(result)
```

## 🔧 Configuration

### Supported File Types

#### Images
- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`, `.webp`

#### Audio
- `.mp3`, `.wav`, `.m4a`, `.flac`, `.aac`, `.ogg`

#### Video
- `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`, `.webm`

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
TEMP_DIR=temp
OUTPUT_DIR=output
LOG_LEVEL=INFO
```

## 🏗️ Project Structure

```
langGraph-game/
├── src/
│   ├── tools/
│   │   ├── base.py              # Base tool class
│   │   ├── ocr_tool.py          # OCR functionality
│   │   ├── transcriber_tool.py  # Audio transcription
│   │   ├── video_compressor_tool.py
│   │   ├── image_compressor_tool.py
│   │   ├── enhancer_tool.py     # Media enhancement
│   │   └── llm_summarizer_tool.py
│   ├── config.py                # Configuration settings
│   ├── graph.py                 # LangChain agent setup
│   └── main.py                  # FastAPI application
├── temp/                        # Temporary file storage
├── output/                      # Processed file output
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🤖 How It Works

1. **File Upload**: Users upload media files through the REST API
2. **Instruction Processing**: Natural language instructions are parsed by GPT-4
3. **Tool Selection**: The AI agent automatically selects appropriate tools
4. **Processing Pipeline**: Tools are executed in the optimal sequence
5. **Result Delivery**: Processed results are returned via JSON response

### AI Agent Architecture

The system uses LangChain's agent framework with:
- **LLM**: OpenAI GPT-4 Turbo for instruction understanding
- **Tools**: Specialized media processing tools
- **Agent Executor**: Orchestrates tool usage and decision making

## 🔍 API Reference

### POST `/process`

Process media files with natural language instructions.

**Parameters:**
- `file` (multipart/form-data): Media file to process
- `instruction` (form field): Natural language processing instruction

**Response:**
```json
{
  "status": "success|error",
  "instruction": "Original instruction",
  "file_type": "Detected MIME type",
  "result": "Processing result or output",
  "message": "Error message if applicable"
}
```

## 🧪 Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

### Code Formatting
```bash
# Install formatting tools
pip install black isort

# Format code
black src/
isort src/
```

### Adding New Tools

1. Create a new tool class inheriting from `BaseTool`
2. Implement the `_arun` method
3. Add the tool to the `MediaProcessingGraph` in `graph.py`

Example:
```python
from .base import BaseTool

class CustomTool(BaseTool):
    name: str = "CustomTool"
    description: str = "Description of what this tool does"
    
    async def _arun(self, input_data: str) -> str:
        # Your tool logic here
        return "processed_result"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

#### FFmpeg Not Found
```bash
# Ensure FFmpeg is in your PATH
ffmpeg -version
```

#### OpenAI API Key Issues
- Verify your API key is correct in the `.env` file
- Check your OpenAI account has sufficient credits

#### Memory Issues with Large Files
- Increase system memory allocation
- Process files in smaller chunks
- Use video compression before other operations

#### Tesseract OCR Issues
```bash
# Verify Tesseract installation
tesseract --version
```

### Getting Help

- Check the [API documentation](http://localhost:8000/docs) when the server is running
- Review logs in the console output
- Open an issue on GitHub for bugs or feature requests

## 🔮 Roadmap

- [ ] Batch processing support
- [ ] Real-time streaming capabilities
- [ ] Additional language support for OCR
- [ ] Custom model integration
- [ ] Web interface for easier interaction
- [ ] Docker containerization
- [ ] Cloud deployment guides

---

**Made with ❤️ using LangChain and FastAPI** 