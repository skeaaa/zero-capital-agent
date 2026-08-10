"""ChatGPT client for LLM interactions."""

import json
from typing import List, Dict, Any, Optional
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
        self.conversation_history: List[Dict[str, str]] = []
        
        # Only initialize OpenAI client if API key is available
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
                self.demo_mode = False
            except Exception as e:
                print(f"Warning: Could not initialize OpenAI client: {e}")
                self.client = None
                self.demo_mode = True
        else:
            self.client = None
            self.demo_mode = True
    
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
        # In demo mode, generate mock responses
        if self.demo_mode or not self.client:
            return self._get_demo_response()
        
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
    
    def _get_demo_response(self) -> str:
        """Generate a demo response based on user input.
        
        Returns:
            Demo response text
        """
        # Get the last user message
        last_user_msg = None
        for msg in reversed(self.conversation_history):
            if msg["role"] == "user":
                last_user_msg = msg["content"].lower()
                break
        
        if not last_user_msg:
            return "Hello! How can I help you today?"
        
        # Generate contextual demo responses
        if "calculate" in last_user_msg or "math" in last_user_msg or "*" in last_user_msg or "+" in last_user_msg:
            # Math calculation detected - attempt to extract and use calculator tool
            return '{"tool": "calculator", "params": {"operation": "add", "a": 25, "b": 10}}'
        elif "python" in last_user_msg or "programming" in last_user_msg:
            return "Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in web development, data science, AI, and automation. Would you like to know more about its applications?"
        elif "agent" in last_user_msg or "ai" in last_user_msg:
            return "An autonomous AI agent is a software system capable of making decisions and taking actions independently based on its training and the environment. These agents can learn from experiences and adapt their behavior over time. The zero-capital agent we're using here operates with built-in safety constraints and doesn't require any financial resources to run."
        elif "search" in last_user_msg or "find" in last_user_msg:
            return '{"tool": "web_search", "params": {"query": "information"}}'
        else:
            return "I understand. Let me help you with that. I have access to tools for calculations, file operations, and information retrieval. How specifically can I assist you?"
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get full conversation history.
        
        Returns:
            List of messages in conversation
        """
        return self.conversation_history.copy()
