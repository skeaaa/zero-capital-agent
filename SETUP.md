# Setup Guide for Zero-Capital Autonomous Agent

## Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### 2. Clone and Install

```bash
# Clone the repository
git clone https://github.com/skeaaa/zero-capital-agent.git
cd zero-capital-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# You can get a free API key at: https://platform.openai.com/api-keys
```

### 4. Run Examples

```bash
# Basic example
python -m examples.basic_agent

# Interactive mode
python -m examples.conversation

# Run a specific task
python -m examples.task_runner "Calculate 100 + 50"
```

## Troubleshooting

### "OPENAI_API_KEY not found"
Make sure your `.env` file exists with a valid API key:
```bash
echo "OPENAI_API_KEY=sk-..." > .env
```

### "Module not found" errors
Ensure you've activated the virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### Installation issues
Try upgrading pip and reinstalling:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Project Structure

- `src/agent.py` - Main agent implementation
- `src/memory.py` - Conversation memory system
- `src/tools/` - Available tools for the agent
- `src/llm/` - ChatGPT API wrapper
- `examples/` - Example scripts and use cases
- `tests/` - Unit tests

## Next Steps

1. Explore the `examples/` directory to see how to use the agent
2. Check `src/tools/` to understand available capabilities
3. Read `README.md` for detailed documentation
4. Run tests: `pytest tests/`

## Safety First

This agent is designed with safety in mind:
- No file modifications by default
- No external API calls beyond ChatGPT
- No arbitrary code execution
- Configurable safety levels in `.env`

Set `SAFE_MODE=true` in your `.env` to enforce all safety constraints.
