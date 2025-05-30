import os
from openai import AsyncOpenAI

# OpenAI API 初始化
BASE_URL = os.getenv("OPENAI_API_BASE", "https://api.deepseek.com")
API_KEY = os.getenv("OPENAI_API_KEY", None)
MODEL = os.getenv("OPENAI_MODEL", "deepseek-chat")

# 检查 API_KEY 是否设置
if not API_KEY:
    raise ValueError("必须设置 OPENAI_API_KEY 来启用问答插件")

openai_client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

async def llm_response(system_prompt:str, question: str) -> str:
    """使用 OpenAI API 获取回答"""
    response = await openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        stream=False
    )
    return response.choices[0].message.content.strip()
