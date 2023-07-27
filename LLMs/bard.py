import asyncio
from BardAPI.bardapi.core import Bard
from concurrent.futures import ThreadPoolExecutor
from llm import LLM
from .llm_capabilities import bard_capabilities

executor = ThreadPoolExecutor(max_workers=1)

async def chat_with_bard(prompt):
    bard = Bard()
    response = bard.get_answer(prompt)
    message = response['content']  # Extract the desired message
    return message

bard_llm = LLM(chat_with_bard, 'Bard', 'Bard', bard_capabilities)
