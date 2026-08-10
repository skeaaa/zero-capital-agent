"""Base class for all agent tools."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseTool(ABC):
    """Abstract base class for tools."""
    
    def __init__(self, name: str, description: str):
        """Initialize a tool.
        
        Args:
            name: Name of the tool
            description: Description of what the tool does
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the tool.
        
        Args:
            **kwargs: Tool-specific parameters
        
        Returns:
            Dictionary with execution result and status
        """
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """Get JSON schema for tool parameters.
        
        Returns:
            JSON schema describing tool parameters
        """
        return {
            "type": "object",
            "properties": {},
            "required": []
        }
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
