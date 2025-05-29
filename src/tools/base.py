from abc import ABC, abstractmethod
from loguru import logger
from langchain_core.tools import BaseTool as LangChainBaseTool

class BaseTool(LangChainBaseTool, ABC):
    name: str
    description: str
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info(f"Initializing {self.name}")
    
    @abstractmethod
    async def _arun(self, input_data: str) -> str:
        """Process the input data and return the result."""
        pass
        
    def _run(self, input_data: str) -> str:
        """Synchronous run is not supported."""
        raise NotImplementedError("Only async operations are supported") 