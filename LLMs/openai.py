import openai
from llm import LLM
from .llm_capabilities import turbo_capabilities, turbo_16k_capabilities, gpt_4_capabilities

async def chat_with_openai(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content']

openai_llm_turbo = LLM(lambda prompt: chat_with_openai(prompt, "gpt-3.5-turbo"), 'OpenAI', 'gpt-3.5-turbo', turbo_capabilities)
openai_llm_turbo_16k = LLM(lambda prompt: chat_with_openai(prompt, "gpt-3.5-turbo-16k"), 'OpenAI', 'gpt-3.5-turbo-16k', turbo_16k_capabilities)
openai_llm_4 = LLM(lambda prompt: chat_with_openai(prompt, "gpt-4"), 'OpenAI', 'gpt-4', gpt_4_capabilities)
