import asyncio
from bookroom_agents.core.tool.base import BaseTool


class TestTool(BaseTool):
    name: str = "test"
    description: str = "This is a test tool."
    parameters: dict = {
        "param": {"type": "string", "description": "A test parameter."},
    }

    async def execute(self, param1: str) -> dict:
        return {"result": f"Received {param1}"}


if __name__ == "__main__":
    test_tool = TestTool()
    result = asyncio.run(test_tool.execute(param="Hello"))
    print(result)
