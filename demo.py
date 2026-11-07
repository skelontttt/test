import os
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError, APITimeoutError, RateLimitError

# 1. 加载环境变量
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"  # 通义千问的话改这里
)


# 2. 封装一个带错误处理函数
def ask(question, retries=2):
    for attempt in range(retries + 1):
        try:
            # 尝试请求
            resp = client.chat.completions.create(
                model="deepseek-chat",  # 通义千问用 qwen-plus
                messages=[{"role": "user", "content": question}],
                timeout=30,  # 设置30秒超时
            )
            return resp.choices[0].message.content

        except RateLimitError:
            # 遇到限流，等待重试
            if attempt < retries:
                wait_time = 2 ** attempt
                print(f"[触发限流] 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
                continue
            return "【错误】请求太频繁，请稍后再试。"

        except APITimeoutError:
            return "【错误】请求超过30秒超时，请检查网络。"

        except APIError as e:
            # 捕获其他 API 错误（如 401 Key错误，402 余额不足）
            return f"【API错误】状态码 {e.status_code}: {e.message}"


# 3. 运行
if __name__ == "__main__":
    question = "用一句话解释FDE是什么"
    print("正在思考中...")
    answer = ask(question)
    print("\n回答：", answer)