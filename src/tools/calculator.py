"""Calculator tool for mathematical operations."""

import math
from typing import Any, Dict
from .base_tool import BaseTool


class Calculator(BaseTool):
    """A tool for performing mathematical calculations."""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs mathematical calculations and operations"
        )
    
    def execute(self, operation: str, a: float = None, b: float = None) -> Dict[str, Any]:
        """Execute mathematical operation.
        
        Args:
            operation: Type of operation (add, subtract, multiply, divide, power, sqrt, etc.)
            a: First operand
            b: Second operand (for binary operations)
        
        Returns:
            Dictionary with result and status
        """
        try:
            result = None
            
            if operation == "add" and a is not None and b is not None:
                result = a + b
            elif operation == "subtract" and a is not None and b is not None:
                result = a - b
            elif operation == "multiply" and a is not None and b is not None:
                result = a * b
            elif operation == "divide" and a is not None and b is not None:
                if b == 0:
                    return {"status": "error", "message": "Division by zero"}
                result = a / b
            elif operation == "power" and a is not None and b is not None:
                result = a ** b
            elif operation == "sqrt" and a is not None:
                if a < 0:
                    return {"status": "error", "message": "Cannot take square root of negative number"}
                result = math.sqrt(a)
            elif operation == "abs" and a is not None:
                result = abs(a)
            else:
                return {"status": "error", "message": f"Unknown operation: {operation}"}
            
            return {
                "status": "success",
                "operation": operation,
                "result": result,
                "message": f"Calculated {operation} result: {result}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Calculation error: {str(e)}"
            }
    
    def get_schema(self) -> Dict[str, Any]:
        """Get JSON schema for calculator parameters."""
        return {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "description": "Operation to perform: add, subtract, multiply, divide, power, sqrt, abs"
                },
                "a": {
                    "type": "number",
                    "description": "First operand"
                },
                "b": {
                    "type": "number",
                    "description": "Second operand (for binary operations)"
                }
            },
            "required": ["operation", "a"]
        }
