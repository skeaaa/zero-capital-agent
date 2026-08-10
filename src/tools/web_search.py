"""Web search tool for information retrieval."""

from typing import Any, Dict, List
from .base_tool import BaseTool


class WebSearch(BaseTool):
    """A tool for web search (simulated for zero-capital mode)."""
    
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Searches for information online"
        )
        # Local knowledge base for zero-capital mode
        self.knowledge_base = {
            "python": "Python is a high-level programming language known for its simplicity and readability.",
            "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
            "chatgpt": "ChatGPT is an AI language model developed by OpenAI.",
            "agent": "An autonomous agent is an AI system that can perform tasks independently.",
        }
    
    def execute(self, query: str) -> Dict[str, Any]:
        """Search for information.
        
        Args:
            query: Search query
        
        Returns:
            Dictionary with search results and status
        """
        try:
            if not query:
                return {"status": "error", "message": "Query parameter required"}
            
            query_lower = query.lower()
            
            # Search in knowledge base
            results = []
            for key, value in self.knowledge_base.items():
                if key in query_lower or query_lower in key:
                    results.append({
                        "title": key.title(),
                        "snippet": value,
                        "relevance": "high" if key in query_lower else "medium"
                    })
            
            if not results:
                return {
                    "status": "success",
                    "query": query,
                    "results": [],
                    "message": "No results found in knowledge base"
                }
            
            return {
                "status": "success",
                "query": query,
                "results": results,
                "count": len(results),
                "message": f"Found {len(results)} result(s)"
            }
        
        except Exception as e:
            return {
                "status": "error",
                "message": f"Search error: {str(e)}"
            }
    
    def get_schema(self) -> Dict[str, Any]:
        """Get JSON schema for web search parameters."""
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                }
            },
            "required": ["query"]
        }
