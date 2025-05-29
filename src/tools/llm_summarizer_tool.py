from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
from typing import Any
from .base import BaseTool

SUMMARIZE_PROMPT = """Below is a text that needs to be summarized. Please provide a clear, concise summary that captures the main points and key information:

{text}

Create a summary that is both informative and easy to understand. Focus on the most important points while maintaining accuracy."""

class LLMSummarizerTool(BaseTool):
    name: str = "LLMSummarizer"
    description: str = "Summarizes text content using LLM"
    llm: Any = None
    prompt: Any = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.3)
        self.prompt = ChatPromptTemplate.from_template(SUMMARIZE_PROMPT)
        
    async def _arun(self, input_data: str) -> str:
        try:
            chain = self.prompt | self.llm
            print("print data in the tool : ", input_data)
            response = await chain.ainvoke({
                "text": input_data
            })
            
            logger.info("Successfully generated summary")
            return response.content.strip()
            
        except Exception as e:
            logger.error(f"Error in summarization: {str(e)}")
            raise