"""
This module contains all server related routes.
"""

from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from bookroom_agents.core.tool.test import TestTool
from bookroom_agents.utils.utils_api import get_api_key_dependency
from bookroom_agents.core.mcp.server import MCPServer

server = MCPServer()
server.register_tool(TestTool())  # Add test tool to the server

router = APIRouter(tags=["mcp"], prefix="/api/mcp")


class McpResponse(BaseModel):
    """MCP Server response model."""

    status: str
    message: str
    item_list: Optional[list] = None


def create_mcp_routes(args: Any, api_key: Optional[str] = None):
    # Create the optional API key dependency
    optional_api_key = get_api_key_dependency(api_key)

    @router.get(
        "/healthy",
        response_model=McpResponse,
        dependencies=[Depends(optional_api_key)]
    )
    async def get_mcp_status():
        """Get current MCP server status."""
        return McpResponse(status="MCP is healthy", message="Mcp is running normally.")
    
    return router
