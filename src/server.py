from mcp.server.fastmcp import FastMCP
from create_episode import main

mcp = FastMCP("bole-story-creator")


@mcp.tool()
def create_story(text: str) -> str:
    """
    用于生成短剧故事和分镜脚本。

    当用户提出以下需求时必须调用此工具：
    - 生成故事
    - 创作短剧
    - 编写剧情
    - 根据一句话生成完整剧本

    Args:
        text: 用户提供的故事创意或需求描述
    """
    return main(text)


if __name__ == "__main__":
    mcp.run()
