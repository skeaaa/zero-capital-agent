"""Memory management system for the autonomous agent."""

from typing import List, Dict, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Turn:
    """Represents a single turn in the conversation."""
    
    user_message: str
    assistant_response: str
    timestamp: datetime = field(default_factory=datetime.now)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class Memory:
    """Memory management system for conversation history."""
    
    def __init__(self, max_turns: int = 50):
        """Initialize memory system.
        
        Args:
            max_turns: Maximum number of turns to keep in memory
        """
        self.max_turns = max_turns
        self.turns: List[Turn] = []
    
    def add_turn(self, user_message: str, assistant_response: str, 
                 tool_calls: List[Dict[str, Any]] = None,
                 metadata: Dict[str, Any] = None) -> None:
        """Add a turn to memory.
        
        Args:
            user_message: User's input message
            assistant_response: Assistant's response
            tool_calls: List of tool calls made
            metadata: Additional metadata
        """
        turn = Turn(
            user_message=user_message,
            assistant_response=assistant_response,
            tool_calls=tool_calls or [],
            metadata=metadata or {}
        )
        self.turns.append(turn)
        
        # Trim if exceeds max turns
        if len(self.turns) > self.max_turns:
            self.turns = self.turns[-self.max_turns:]
    
    def get_context(self, num_turns: int = None) -> str:
        """Get conversation context for the agent.
        
        Args:
            num_turns: Number of recent turns to include. If None, uses all.
        
        Returns:
            Formatted conversation history
        """
        if num_turns:
            relevant_turns = self.turns[-num_turns:]
        else:
            relevant_turns = self.turns
        
        context = []
        for turn in relevant_turns:
            context.append(f"User: {turn.user_message}")
            context.append(f"Assistant: {turn.assistant_response}")
        
        return "\n".join(context)
    
    def clear(self) -> None:
        """Clear all memory."""
        self.turns = []
    
    def get_turns_count(self) -> int:
        """Get number of turns in memory."""
        return len(self.turns)
    
    def get_summary(self) -> str:
        """Get summary of conversation topics."""
        if not self.turns:
            return "No conversation history"
        
        topics = []
        for turn in self.turns:
            # Extract first 50 chars as topic
            topic = turn.user_message[:50]
            if len(turn.user_message) > 50:
                topic += "..."
            topics.append(topic)
        
        return f"Conversation history ({len(self.turns)} turns):\n" + "\n".join(topics)
