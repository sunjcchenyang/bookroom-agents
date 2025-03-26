# 写一个调用mcp server 的客户端代码
class MCPClient:
    def __init__(self, url: str):
        self.url = url
    async def call_tool(self, tool_name: str, **kwargs):
        # 这里需要实现具体的调用逻辑，比如使用http请求或者websocket等
        pass
    