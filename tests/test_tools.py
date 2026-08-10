"""Tests for agent tools."""

import pytest
import os
from src.tools.calculator import Calculator
from src.tools.file_operations import FileOperations
from src.tools.web_search import WebSearch


class TestCalculator:
    """Test calculator tool."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition."""
        result = self.calc.execute(operation="add", a=5, b=3)
        assert result["result"] == 8
    
    def test_subtract(self):
        """Test subtraction."""
        result = self.calc.execute(operation="subtract", a=10, b=3)
        assert result["result"] == 7
    
    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.execute(operation="multiply", a=4, b=5)
        assert result["result"] == 20


class TestFileOperations:
    """Test file operations tool."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.file_ops = FileOperations()
    
    def test_list_current_directory(self):
        """Test listing current directory."""
        result = self.file_ops.execute(operation="list", path=".")
        assert result["status"] == "success"
        assert "files" in result
        assert "directories" in result
    
    def test_nonexistent_file(self):
        """Test reading nonexistent file."""
        result = self.file_ops.execute(operation="read", path="nonexistent.txt")
        assert result["status"] == "error"


class TestWebSearch:
    """Test web search tool."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.search = WebSearch()
    
    def test_search_python(self):
        """Test searching for python."""
        result = self.search.execute(query="python")
        assert result["status"] == "success"
        assert result["count"] > 0
    
    def test_search_ai(self):
        """Test searching for AI."""
        result = self.search.execute(query="ai")
        assert result["status"] == "success"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
