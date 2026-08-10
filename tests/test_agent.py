"""Tests for the autonomous agent."""

import pytest
from src.agent import AutonomousAgent
from src.memory import Memory
from src.tools.calculator import Calculator


class TestMemory:
    """Test the memory system."""
    
    def test_memory_initialization(self):
        """Test memory initialization."""
        memory = Memory(max_turns=10)
        assert memory.max_turns == 10
        assert memory.get_turns_count() == 0
    
    def test_add_turn(self):
        """Test adding turns to memory."""
        memory = Memory()
        memory.add_turn("Hello", "Hi there!")
        assert memory.get_turns_count() == 1
    
    def test_memory_trim(self):
        """Test that memory trims old turns."""
        memory = Memory(max_turns=3)
        for i in range(5):
            memory.add_turn(f"Turn {i}", f"Response {i}")
        assert memory.get_turns_count() == 3


class TestCalculator:
    """Test the calculator tool."""
    
    def test_calculator_initialization(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.name == "calculator"
    
    def test_calculator_add(self):
        """Test addition operation."""
        calc = Calculator()
        result = calc.execute(operation="add", a=2, b=3)
        assert result["status"] == "success"
        assert result["result"] == 5
    
    def test_calculator_divide_by_zero(self):
        """Test division by zero error."""
        calc = Calculator()
        result = calc.execute(operation="divide", a=10, b=0)
        assert result["status"] == "error"
        assert "Division by zero" in result["message"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
