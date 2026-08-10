#!/usr/bin/env python
"""Basic example of the autonomous agent in action."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import AutonomousAgent
from src.config import Config


def main():
    """Run a basic agent conversation."""
    print("\n" + "="*60)
    print("Zero-Capital Autonomous Agent - Basic Example")
    print("="*60 + "\n")
    
    # Check configuration
    if Config.is_demo_mode():
        print("⚠️  Running in DEMO MODE (no OpenAI API key configured)")
        print("   Set OPENAI_API_KEY in .env to use real ChatGPT")
        print()
    else:
        print("✓ Using OpenAI API")
        print()
    
    # Create agent
    agent = AutonomousAgent()
    print(f"Agent initialized: {agent.name}")
    print(f"Safe Mode: {agent.safe_mode}")
    print(f"Available tools: {[tool.name for tool in agent.tools]}")
    print()
    
    # Example tasks
    tasks = [
        "Calculate 25 * 4 + 10",
        "Tell me about Python programming",
        "What is an AI agent?"
    ]
    
    for task in tasks:
        print(f"\nUser: {task}")
        print("-" * 40)
        response = agent.process(task)
        print(f"Agent: {response}")
    
    # Show memory summary
    print("\n" + "="*60)
    print("Memory Summary:")
    print("="*60)
    print(agent.get_memory_summary())
    
    print("\n" + "="*60)
    print("Demo completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
