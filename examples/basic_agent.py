#!/usr/bin/env python
"""Basic example of the autonomous agent in action."""

from src.agent import AutonomousAgent


def main():
    """Run a basic agent conversation."""
    print("\n" + "="*60)
    print("Zero-Capital Autonomous Agent - Basic Example")
    print("="*60 + "\n")
    
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


if __name__ == "__main__":
    main()
