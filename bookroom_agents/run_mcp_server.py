import argparse
from bookroom_agents.core.mcp.server import MCPServer
from bookroom_agents.core.tool.test import TestTool

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server host address (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5002,
        help="Server port number (default: 5002)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Logging level (default: INFO)",
    )

    parser.add_argument(
        "--transport",
        choices=["stdio","sse"],
        default="stdio",
        help="Communication method: stdio or sse (default: stdio)",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    # Create and run server (maintaining original flow)
    server = MCPServer(name="TestServer", host=args.host, port=args.port, log_level=args.log_level)
    server.register_tool(TestTool())  # Add test tool to the server
    server.run(transport=args.transport)
