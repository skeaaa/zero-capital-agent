"""Main autonomous agent implementation."""

import json
import re
from typing import List, Dict, Any, Optional
from src.config import Config
from src.memory import Memory
from src.llm.chatgpt_client import ChatGPTClient
from src.tools.base_tool import BaseTool
from src.tools.calculator import Calculator
from src.tools.file_operations import FileOperations
from src.tools.web_search import WebSearch


class AutonomousAgent:
    """Autonomous agent powered by ChatGPT."""
    
    def __init__(self, name: str = None, tools: List[BaseTool] = None):
        """Initialize the autonomous agent.
        
        Args:
            name: Agent name. If None, uses AGENT_NAME from config
            tools: List of tools available to the agent
        """
        Config.validate()
        
        self.name = name or Config.AGENT_NAME
        self.max_iterations = Config.MAX_ITERATIONS
        self.safe_mode = Config.SAFE_MODE
        
        # Initialize LLM client
        self.llm = ChatGPTClient()
        
        # Initialize memory
        self.memory = Memory(max_turns=Config.MAX_MEMORY_TURNS)
        
        # Initialize tools
        if tools is None:
            self.tools = self._get_default_tools()
        else:
            self.tools = tools
        
        self.tool_map = {tool.name: tool for tool in self.tools}
        
        # Setup system prompt
        self._setup_system_prompt()
    
    def _get_default_tools(self) -> List[BaseTool]:
        """Get default set of tools.
        
        Returns:
            List of default tools
        """
        return [
            Calculator(),
            FileOperations(),
            WebSearch(),
        ]
    
    def _setup_system_prompt(self) -> None:
        """Setup the system prompt for the agent."""
        tools_description = self._format_tools_description()
        
        system_prompt = f"""You are {self.name}, an autonomous AI agent.

Your purpose is to help the user by:
1. Understanding their requests
2. Planning the steps needed
3. Using available tools to accomplish tasks
4. Reasoning about results
5. Providing clear responses

Available Tools:
{tools_description}

Instructions:
- Think step-by-step about each task
- Use tools when necessary to gather information or perform calculations
- Format tool calls as: {{"tool": "tool_name", "params": {{"key": "value"}}}}
- Be honest about limitations
- Prioritize safety and user privacy
- If in doubt, ask for clarification

Safe Mode: {self.safe_mode}
- No file modifications
- No external API calls beyond provided tools
- No execution of arbitrary code
"""
        self.llm.add_system_message(system_prompt)
    
    def _format_tools_description(self) -> str:
        """Format tools description for the system prompt.
        
        Returns:
            Formatted tools description
        """
        descriptions = []
        for tool in self.tools:
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)
    
    def _parse_tool_calls(self, response: str) -> List[Dict[str, Any]]:
        """Parse tool calls from response.
        
        Args:
            response: Response text from LLM
        
        Returns:
            List of parsed tool calls
        """
        tool_calls = []
        
        # Look for JSON-formatted tool calls
        pattern = r'\{"tool"\s*:\s*"([^"]+)"\s*,\s*"params"\s*:\s*(\{[^}]+\})\}'
        matches = re.finditer(pattern, response)
        
        for match in matches:
            try:
                tool_name = match.group(1)
                params = json.loads(match.group(2))
                tool_calls.append({
                    "tool": tool_name,
                    "params": params
                })
            except (json.JSONDecodeError, AttributeError):
                continue
        
        return tool_calls
    
    def _execute_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool.
        
        Args:
            tool_name: Name of the tool to execute
            params: Tool parameters
        
        Returns:
            Tool execution result
        """
        if tool_name not in self.tool_map:
            return {
                "status": "error",
                "message": f"Unknown tool: {tool_name}"
            }
        
        tool = self.tool_map[tool_name]
        try:
            return tool.execute(**params)
        except Exception as e:
            return {
                "status": "error",
                "message": f"Tool execution error: {str(e)}"
            }
    
    def process(self, user_input: str) -> str:
        """Process a user input and generate a response.
        
        Args:
            user_input: User's input message
        
        Returns:
            Agent's response
        """
        self.llm.add_user_message(user_input)
        
        iteration = 0
        while iteration < self.max_iterations:
            iteration += 1
            
            # Get response from LLM
            response = self.llm.get_response()
            
            # Check for tool calls
            tool_calls = self._parse_tool_calls(response)
            
            if not tool_calls:
                # No tool calls, this is the final response
                self.memory.add_turn(
                    user_message=user_input,
                    assistant_response=response,
                    metadata={"iterations": iteration}
                )
                return response
            
            # Execute tools and add results back
            tool_results = []
            for call in tool_calls:
                result = self._execute_tool(call["tool"], call["params"])
                tool_results.append({
                    "tool": call["tool"],
                    "params": call["params"],
                    "result": result
                })
            
            # Format tool results for the agent
            results_text = "Tool execution results:\n"
            for result in tool_results:
                results_text += f"\n{result['tool']} with params {result['params']}:\n"
                results_text += json.dumps(result['result'], indent=2)
            
            # Add tool results back to conversation
            self.llm.add_assistant_message(response)
            self.llm.add_user_message(results_text)
        
        # Max iterations reached
        response = "Max iterations reached. Please try a simpler task."
        self.memory.add_turn(
            user_message=user_input,
            assistant_response=response,
            metadata={"iterations": self.max_iterations, "status": "max_iterations_reached"}
        )
        return response
    
    def add_tool(self, tool: BaseTool) -> None:
        """Add a tool to the agent.
        
        Args:
            tool: Tool to add
        """
        self.tools.append(tool)
        self.tool_map[tool.name] = tool
        # Update system prompt with new tools
        self._setup_system_prompt()
    
    def get_memory_summary(self) -> str:
        """Get summary of conversation memory.
        
        Returns:
            Memory summary
        """
        return self.memory.get_summary()
    
    def clear_memory(self) -> None:
        """Clear conversation memory."""
        self.memory.clear()
        # Keep system prompt
        self.llm.conversation_history = [
            self.llm.conversation_history[0]  # Keep system message
        ]
