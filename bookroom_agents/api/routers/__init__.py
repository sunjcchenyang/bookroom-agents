"""
This module contains all the routers for the API.
"""

from .server_routes import router as server_router
from .mcp_routes import router as mcp_router

__all__ = [
    "server_router"
    "mcp_router"
]
