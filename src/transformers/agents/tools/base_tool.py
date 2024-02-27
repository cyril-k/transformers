from abc import abstractmethod
from typing import Any

class BaseTool:
    name: str
    description: str
    parameters: list

    @abstractmethod
    def to_prompt(self, *args: Any, **kwds: Any) -> Any:
        "Returns formatted tool description"

    @abstractmethod
    def parse_args(self, *args: Any, **kwds: Any) -> Any:
        "Attempts to parse tool input from LLM message"

    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        "Runs the tool"

    @abstractmethod
    @classmethod
    def from_hub(cls, *args: Any, **kwds: Any):
        "Loads the tool from hub"
        return cls
    
    @abstractmethod
    def to_hub():
        "Pushes the tool to hub"