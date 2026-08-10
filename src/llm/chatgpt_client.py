"""ChatGPT client for LLM interactions."""

import json
from typing import List, Dict, Any, Optional
from openai import OpenAI
from src.config import Config


class ChatGPTClient:
    """Client for interacting with ChatGPT API."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = None):
        """Initialize ChatGPT client.
        
        Args:
            api_key: OpenAI API key. If None, uses OPENAI_API_KEY from config
            model: Model to use. If None, uses AGENT_MODEL from config
        """
        self.api_key = api_key or Config.OPENAI_API_KEY
        self.model = model or Config.AGENT_MODEL
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history: List[Dict[str, str]] = []
    
    def add_system_message(self, message: str) -> None:
        """Add a system message to conversation history.
        
        Args:
            message: System message content
        """
        self.conversation_history.append({
            "role": "system",
            "content": message
        })
    
    def add_user_message(self, message: str) -> None:
        """Add a user message to conversation history.
        
        Args:
            message: User message content
        """
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
    
    def add_assistant_message(self, message: str) -> None:
        """Add an assistant message to conversation history.
        
        Args:
            message: Assistant message content
        """
        self.conversation_history.append({
            "role": "assistant",
            "content": message
        })
    
    def get_response(self, temperature: float = 0.7, max_tokens: int = 1000) -> str:
        """Get response from ChatGPT.
        
        Args:
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
        
        Returns:
            Assistant's response text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except Exception as e:
            raise RuntimeError(f"Error getting response from ChatGPT: {str(e)}")
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get full conversation history.
        
        Returns:
            List of messages in conversation
        """
        return self.conversation_history.copy()
