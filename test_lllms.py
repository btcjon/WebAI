import asyncio
from LLMs import bing_llm, openai_llm_turbo, bard_llm

# Bing LLM Test
async def test_bing_llm():
    response = await bing_llm.chat("Hello")
    assert response is not None and response != "", "Bing LLM did not return a response."

# OpenAI LLM Test
async def test_openai_llm():
    response = await openai_llm_turbo.chat("Hello")
    assert response is not None and response != "", "OpenAI LLM did not return a response."

# Bard LLM Test
async def test_bard_llm():
    response = await bard_llm.chat("Hello")
    assert response is not None and response != "", "Bard LLM did not return a response."

# Run the tests
asyncio.run(test_bing_llm())
asyncio.run(test_openai_llm())
asyncio.run(test_bard_llm())
