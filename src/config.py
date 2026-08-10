"""Configuration management for the zero-capital agent."""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for the agent."""

    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AGENT_MODEL: str = os.getenv("AGENT_MODEL", "gpt-3.5-turbo")
    
    # Agent Configuration
    AGENT_NAME: str = os.getenv("AGENT_NAME", "ZeroCapitalAgent")
    MAX_MEMORY_TURNS: int = int(os.getenv("MAX_MEMORY_TURNS", "50"))
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "10"))
    
    # Safety Configuration
    SAFE_MODE: bool = os.getenv("SAFE_MODE", "true").lower() == "true"
    ALLOW_FILE_WRITES: bool = os.getenv("ALLOW_FILE_WRITES", "false").lower() == "true"
    ALLOW_EXTERNAL_APIS: bool = os.getenv("ALLOW_EXTERNAL_APIS", "false").lower() == "true"
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """Validate configuration."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set in environment variables")
        return True
