import logging

from bookroom_agents.api import __api_name__


def setup_logger():
    """Setup the logger for the application."""
    logger = logging.getLogger(__api_name__)
    # 创建一个 StreamHandler 将日志输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # 创建一个格式化器并将其添加到处理器中
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stream_handler.setFormatter(formatter)
    # 将处理器添加到 logger 中
    logger.addHandler(stream_handler)

    return logger


logger = setup_logger()
