# Zero-Capital Autonomous Agent

An autonomous AI agent powered by ChatGPT that can perform tasks with zero financial outlay. The agent makes intelligent decisions, executes tools safely, and manages its own workflow without capital requirements.

## Features

- **Autonomous Decision-Making**: Uses ChatGPT to analyze situations and make intelligent decisions
- **Tool Execution**: Safely executes predefined tools and plugins
- **Memory Management**: Maintains context and learns from interactions
- **Safe Operation**: Built-in safety constraints to prevent harmful actions
- **Extensible Architecture**: Easy to add new tools and capabilities
- **No Capital Required**: Operates without financial transactions or API costs (uses free tier compatible architecture)

## Project Structure

```
zero-capital-agent/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── __init__.py
│   ├── agent.py              # Main agent logic
│   ├── memory.py             # Memory management system
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── base_tool.py      # Base tool class
│   │   ├── web_search.py     # Web search tool
│   │   ├── file_operations.py # File operations
│   │   ├── code_execution.py # Safe code execution
│   │   └── calculator.py     # Mathematical calculations
│   ├── llm/
│   │   ├── __init__.py
│   │   └── chatgpt_client.py # ChatGPT API wrapper
│   └── config.py             # Configuration management
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   └── test_tools.py
└── examples/
    ├── basic_agent.py        # Basic example
    ├── task_runner.py        # Run autonomous tasks
    └── conversation.py       # Interactive conversation
```

## Setup

### Prerequisites
- Python 3.8+
- OpenAI API key (free tier)
- Internet connection

### Installation

1. Clone the repository:
```bash
git clone https://github.com/skeaaa/zero-capital-agent.git
cd zero-capital-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Configuration

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
AGENT_NAME=ZeroCapitalAgent
AGENT_MODEL=gpt-3.5-turbo
MAX_MEMORY_TURNS=50
SAFE_MODE=true
```

## Usage

### Run a Basic Agent Conversation

```bash
python -m examples.basic_agent
```

### Run Autonomous Tasks

```bash
python -m examples.task_runner "Your task here"
```

### Interactive Mode

```bash
python -m examples.conversation
```

## How It Works

1. **User Input**: Receives a task or question
2. **Analysis**: Agent analyzes the input using ChatGPT
3. **Planning**: Determines which tools are needed
4. **Execution**: Safely executes tools with constraints
5. **Reasoning**: Uses results to make further decisions
6. **Response**: Provides intelligent response to user
7. **Memory**: Stores context for future interactions

## Safety Constraints

- No external API calls (uses free/local resources only)
- No file system modifications without explicit approval
- No execution of untrusted code
- Rate limiting to prevent abuse
- Configurable safety levels

## Tools Available

- **Web Search**: Search for information (local database compatible)
- **Calculator**: Perform mathematical calculations
- **File Operations**: Read and list files safely
- **Code Execution**: Run safe Python code with restrictions

## Testing

Run the test suite:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Troubleshooting

### "OpenAI API key not found"
Make sure your `.env` file exists and contains `OPENAI_API_KEY=your_key_here`

### "Module not found"
Ensure you've activated the virtual environment and installed requirements

### Agent not responding
Check that you have internet connectivity and your API key is valid

## Future Roadmap

- [ ] Multi-agent collaboration
- [ ] Advanced memory with vector databases
- [ ] Integration with external APIs (safely)
- [ ] Web interface for agent control
- [ ] Plugin system for custom tools
- [ ] Monitoring and logging dashboard
