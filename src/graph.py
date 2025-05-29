from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from loguru import logger

from .tools.ocr_tool import OCRTool
from .tools.transcriber_tool import TranscriberTool
from .tools.video_compressor_tool import VideoCompressorTool
from .tools.image_compressor_tool import ImageCompressorTool
from .tools.enhancer_tool import EnhancerTool
from .tools.llm_summarizer_tool import LLMSummarizerTool

class MediaProcessingGraph:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
        self.tools = [
            OCRTool(),
            TranscriberTool(),
            VideoCompressorTool(),
            ImageCompressorTool(),
            EnhancerTool(),
            LLMSummarizerTool()
        ]
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a media processing assistant. You have access to the following tools: OCR, Transcriber, VideoCompressor, ImageCompressor, Enhancer, LLMSummarizer. Use them as needed to fulfill the user's instruction."),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        self.agent = create_openai_tools_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    async def process_media(self, instruction: str, file_path: str, file_type: str) -> dict:
        user_input = f"{instruction}\nFile path: {file_path}\nFile type: {file_type}"
        try:
            result = await self.agent_executor.ainvoke({"input": user_input})
            logger.info(f"Agent result: {result}")
            return {"status": "success", "result": result.get("output", "")}
        except Exception as e:
            logger.error(f"Error in agent execution: {str(e)}")
            return {"status": "error", "message": str(e)} 