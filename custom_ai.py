
import asyncio
import os
from dataclasses import dataclass
from typing import Any

import logfire
from devtools import debug
from httpx import AsyncClient

from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


llm = 'deepseek/deepseek-r1-zero:free'
api = 'sk-or-v1-1ef885c6827ac8356284ca05885e99885939d7cd2f087f9c860f20dd8350f4fb33'
model = OpenAIModel(llm, base_url = 'https://openrouter.ai/api/v1', api_key=api)
agent = Agent(model)

async def main():
    async with AsyncClient() as client:
        result = await agent.run(
            'Tell me a funny story'
        )
        print('Response:', result.data)

if __name__ == '__main__':
    asyncio.run(main())
