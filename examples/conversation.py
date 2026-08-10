#!/usr/bin/env python
"""Interactive conversation with the autonomous agent."""

import sys
from src.agent import AutonomousAgent


def main():
    """Run interactive conversation with the agent."""
    print("\n" + "="*60)
    print("Zero-Capital Autonomous Agent - Interactive Mode")
    print("="*60)
    print("Type 'quit' to exit, 'memory' to see conversation summary\n")
    
    # Create agent
    agent = AutonomousAgent()
    print(f"Agent: {agent.name} initialized and ready.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "quit":
                print("\nAgent: Goodbye! Have a great day.")
                break
            
            if user_input.lower() == "memory":
                print("\n" + agent.get_memory_summary())
                continue
            
            print()
            response = agent.process(user_input)
            print(f"Agent: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nAgent: Interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
