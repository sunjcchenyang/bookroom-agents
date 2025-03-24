import asyncio
from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, HTTPException, Request, Response
from dotenv import load_dotenv, find_dotenv
from fastapi.middleware.cors import CORSMiddleware
from ascii_colors import ASCIIColors
from fastapi.responses import JSONResponse
import uvicorn

from bookroom_agents.api.routers.mcp_routes import create_mcp_routes
from bookroom_agents.api.routers.server_routes import create_server_routes
from bookroom_agents.utils.utils_api import (
    get_cors_origins,
    parse_args,
    logger,
)
from bookroom_agents.api import __api_name__, __api_description__, __api_version__

# 确保环境变量已加载
load_dotenv(find_dotenv(), override=True)


# 创建一个全局锁
global_lock = asyncio.Lock()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Store background tasks
    app.state.background_tasks = set()
    try:
        async with global_lock:
            # task = asyncio.create_task(run_model_loaded_process(args))
            # task.add_done_callback(app.state.background_tasks.discard)
            logger.info(f"Process {os.getpid()} auto scan task started at startup.")
        ASCIIColors.green("\nServer is ready to accept connections! 🚀\n")
        yield
    finally:
        async with global_lock:
            # 取消所有后台任务
            for task in app.state.background_tasks:
                task.cancel()
        ASCIIColors.green("\nServer is shutting down! 🛑\n")


def create_app(args) -> FastAPI:
    openapi_tags = [
        {"name": "server", "description": "Server routes for server."},
        {"name": "mcp", "description": "API routes for MCP."},
    ]
    """Create a new FastAPI application instance"""
    app = FastAPI(
        title=__api_name__,
        description=__api_description__,
        version=__api_version__,
        openapi_url="/openapi.json",  # Explicitly set OpenAPI schema URL
        docs_url="/docs",  # Explicitly set docs URL
        redoc_url="/redoc",  # Explicitly set redoc URL
        openapi_tags=[*openapi_tags],
        lifespan=lifespan,
        contact={"name": "sndraw", "url": "https://github.com/sndraw"},
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=get_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if args.debug:
        app.debug = True

    api_key = args.key

    # Add SSL validation
    if args.ssl:
        if not args.ssl_certfile or not args.ssl_keyfile:
            raise Exception(
                "SSL certificate and key files must be provided when SSL is enabled"
            )
        if not os.path.exists(args.ssl_certfile):
            raise Exception(f"SSL certificate file not found: {args.ssl_certfile}")
        if not os.path.exists(args.ssl_keyfile):
            raise Exception(f"SSL key file not found: {args.ssl_keyfile}")

    # 自定义错误处理程序
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        headers = {}
        if exc.headers is not None:
            headers = {**exc.headers}
        return JSONResponse(
            status_code=exc.status_code,
            headers={
                **headers,
            },
            content={
                "error": {
                    "code": None,
                    "message": exc.detail,
                    "pram": None,
                    "type": "server_error",
                }
            },
        )

    app.include_router(create_server_routes(args, api_key))
    app.include_router(create_mcp_routes(args, api_key))

    return app


args = parse_args()

app = create_app(args)


def main():
    # Start Uvicorn in single process mode
    uvicorn_config = {"host": args.host, "port": args.port}
    
    if args.reload:
        uvicorn_config["reload"] = True
    if args.workers > 1:
        uvicorn_config["workers"] = args.workers

    if args.ssl:
        uvicorn_config.update(
            {
                "ssl_certfile": args.ssl_certfile,
                "ssl_keyfile": args.ssl_keyfile,
            }
        )

    if args.debug:
        ASCIIColors.yellow("\nServer is running in debug mode! \n")

    uvicorn.run("bookroom_agents.server:app", **uvicorn_config)


if __name__ == "__main__":
    main()
