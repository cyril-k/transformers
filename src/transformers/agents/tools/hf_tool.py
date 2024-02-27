from .base_tool import BaseTool
from typing import Any, List

class Parameter:

    def __init__(
            self, 
            type: str, 
            description: str, 
            required: bool
        ):

        if type not in ["string", "number", "integer", "object", "array", "boolean"]:
            raise ValueError(f"Unsupported parameter type {type}.")
        
        self.type = type
        self.description = description
        self.required = required

class HFTool(BaseTool):

    def __init__(
            self, 
            name: str, 
            description: str, 
            parameters: List[Parameter], 
            tool: callable
        ):

        self.name = name
        self.description = description
        self.parameters = parameters
        self._tool = tool

