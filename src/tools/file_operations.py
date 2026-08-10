"""File operations tool for safe file handling."""

import os
from typing import Any, Dict, List
from .base_tool import BaseTool


class FileOperations(BaseTool):
    """A tool for safe file operations."""
    
    def __init__(self, allowed_base_path: str = "."):
        super().__init__(
            name="file_operations",
            description="Performs safe file operations (read, list)"
        )
        self.allowed_base_path = os.path.abspath(allowed_base_path)
    
    def _is_safe_path(self, path: str) -> bool:
        """Check if path is within allowed base path.
        
        Args:
            path: Path to check
        
        Returns:
            True if path is safe, False otherwise
        """
        abs_path = os.path.abspath(path)
        return abs_path.startswith(self.allowed_base_path)
    
    def execute(self, operation: str, path: str = None, content: str = None) -> Dict[str, Any]:
        """Execute file operation.
        
        Args:
            operation: Type of operation (read, list, info)
            path: File or directory path
            content: Content to write (not implemented for safety)
        
        Returns:
            Dictionary with operation result and status
        """
        try:
            if not path:
                return {"status": "error", "message": "Path parameter required"}
            
            if not self._is_safe_path(path):
                return {"status": "error", "message": "Access denied: path outside allowed directory"}
            
            if operation == "read":
                if not os.path.isfile(path):
                    return {"status": "error", "message": f"File not found: {path}"}
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    return {
                        "status": "success",
                        "operation": "read",
                        "path": path,
                        "content": content,
                        "size": len(content)
                    }
                except UnicodeDecodeError:
                    return {"status": "error", "message": "File is not UTF-8 encoded"}
            
            elif operation == "list":
                if not os.path.isdir(path):
                    return {"status": "error", "message": f"Directory not found: {path}"}
                
                items = os.listdir(path)
                files = []
                dirs = []
                
                for item in items:
                    item_path = os.path.join(path, item)
                    if os.path.isdir(item_path):
                        dirs.append(item)
                    else:
                        files.append(item)
                
                return {
                    "status": "success",
                    "operation": "list",
                    "path": path,
                    "directories": dirs,
                    "files": files,
                    "total_items": len(items)
                }
            
            elif operation == "info":
                if not os.path.exists(path):
                    return {"status": "error", "message": f"Path not found: {path}"}
                
                stat_info = os.stat(path)
                return {
                    "status": "success",
                    "operation": "info",
                    "path": path,
                    "is_file": os.path.isfile(path),
                    "is_dir": os.path.isdir(path),
                    "size": stat_info.st_size,
                    "modified": stat_info.st_mtime
                }
            
            else:
                return {"status": "error", "message": f"Unknown operation: {operation}"}
        
        except Exception as e:
            return {
                "status": "error",
                "message": f"File operation error: {str(e)}"
            }
    
    def get_schema(self) -> Dict[str, Any]:
        """Get JSON schema for file operations parameters."""
        return {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "description": "Operation to perform: read, list, info"
                },
                "path": {
                    "type": "string",
                    "description": "File or directory path"
                }
            },
            "required": ["operation", "path"]
        }
