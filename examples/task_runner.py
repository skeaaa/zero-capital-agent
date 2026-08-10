#!/usr/bin/env python
"""Run autonomous tasks with the agent."""

import sys
from src.agent import AutonomousAgent


def run_task(task: str):
    """Run a single autonomous task.
    
    Args:
        task: Task description
    """
    print("\n" + "="*60)
    print("Zero-Capital Autonomous Agent - Task Runner")
    print("="*60 + "\n")
    
    print(f"Task: {task}\n")
    
    # Create and run agent
    agent = AutonomousAgent()
    response = agent.process(task)
    
    print(f"\nResult:\n{response}")
    print("\n" + "="*60)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m examples.task_runner <task>")
        print("Example: python -m examples.task_runner 'Calculate 50 * 2'")
        sys.exit(1)
    
    task = " ".join(sys.argv[1:])
    run_task(task)


if __name__ == "__main__":
    main()
