#!/usr/bin/env python
"""Demo mode simulator - shows what the agent does without API key."""

import sys
import os

# Simulate the agent behavior in demo mode
def simulate_agent_response(user_input):
    """Generate demo responses based on user input."""
    user_lower = user_input.lower()
    
    if "calculate" in user_lower or "25 * 4" in user_input or "+" in user_input:
        return 'I can help you calculate that. Using the calculator tool: {"tool": "calculator", "params": {"operation": "multiply", "a": 25, "b": 4}}'
    elif "python" in user_lower or "programming" in user_lower:
        return "Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in web development, data science, AI, and automation. Python's syntax emphasizes code readability and allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java."
    elif "agent" in user_lower or "ai" in user_lower:
        return "An autonomous AI agent is a software system capable of making decisions and taking actions independently based on its training and the environment. These agents can learn from experiences and adapt their behavior over time. The zero-capital agent we're using operates with built-in safety constraints and doesn't require any financial resources to run. It uses tools like calculators, file operations, and knowledge retrieval to accomplish tasks."
    return "I'm ready to assist you. How can I help?"


def main():
    """Run the demo."""
    print("\n" + "="*60)
    print("Zero-Capital Autonomous Agent - Basic Example")
    print("="*60 + "\n")
    print("⚠️  Running in DEMO MODE (no OpenAI API key configured)")
    print("   Set OPENAI_API_KEY in .env to use real ChatGPT\n")
    
    print("Agent initialized: ZeroCapitalAgent")
    print("Safe Mode: True")
    print("Available tools: ['calculator', 'file_operations', 'web_search']")
    print()
    
    tasks = [
        "Calculate 25 * 4 + 10",
        "Tell me about Python programming",
        "What is an AI agent?"
    ]
    
    responses = []
    for task in tasks:
        print(f"\nUser: {task}")
        print("-" * 40)
        response = simulate_agent_response(task)
        responses.append((task, response))
        print(f"Agent: {response}")
    
    print("\n" + "="*60)
    print("Memory Summary:")
    print("="*60)
    print(f"Conversation history ({len(responses)} turns):")
    for i, (task, _) in enumerate(responses, 1):
        summary = task[:50] + ("..." if len(task) > 50 else "")
        print(f"{i}. {summary}")
    
    print("\n" + "="*60)
    print("Demo completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
