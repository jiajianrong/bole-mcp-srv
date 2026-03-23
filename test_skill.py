import json
import subprocess
import os

# 设置环境变量
# os.environ['BOLE_ACCESS_KEY'] = 'test_key'  # 这里使用测试密钥，实际测试时需要替换为真实密钥

# 测试输入
input_data = {
    "text": "生成掩耳盗铃的故事"
}

# 转换为JSON字符串
input_json = json.dumps(input_data)

# 调用技能
result = subprocess.run(
    ['python', 'bole-story-skills/scripts/main.py', input_json],
    capture_output=True,
    text=True
)

# 输出结果
print("Return code:", result.returncode)
print(" stdout:", result.stdout)
print(" stderr:", result.stderr)

# 解析输出
if result.stdout:
    try:
        output = json.loads(result.stdout)
        print("Parsed output:", json.dumps(output, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print("Failed to parse output as JSON")
