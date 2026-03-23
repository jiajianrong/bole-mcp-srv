# Bole Story Creator Skill

一个用于调用博乐AI平台生成短剧故事的 OpenClaw 技能。

## 功能介绍

该技能可以：
- 根据用户提供的故事创意生成完整的短剧故事
- 自动创建分镜脚本
- 生成视频内容
- 返回故事创作结果和视频链接

## 使用方法

### 环境变量配置

需要设置以下环境变量：

```bash
BOLE_ACCESS_KEY=your_bole_access_key
```

### 调用方式

作为 OpenClaw 技能调用：

```python
{
  "text": "生成一个关于友谊的故事"
}
```

### 示例输入输出

**输入：**
```json
{
  "text": "生成乌鸦喝水的故事"
}
```

**输出：**
```json
{
  "result": "故事创作完成！projectId=2033716579396616193, episodeId=1234567890, workspaceId=0987654321。控制台链接：https://bole.bonanai.com/story/2033716579396616193?episodeId=1234567890 。视频链接：https://example.com/video.mp4"
}
```

## 注意事项

1. 调用前请确保已设置有效的 `BOLE_ACCESS_KEY`
2. 生成过程可能需要较长时间，请耐心等待
3. 输出结果包含项目信息和视频链接，可直接访问查看
