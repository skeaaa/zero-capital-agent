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
    
    # Demo Mode (fallback when API key not available)
    DEMO_MODE: bool = os.getenv("DEMO_MODE", "true").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """Validate configuration."""
        if not cls.OPENAI_API_KEY and not cls.DEMO_MODE:
            raise ValueError("OPENAI_API_KEY not set in environment variables and DEMO_MODE is disabled")
        return True
    
    @classmethod
    def is_demo_mode(cls) -> bool:
        """Check if running in demo mode."""
        return not cls.OPENAI_API_KEY and cls.DEMO_MODE
