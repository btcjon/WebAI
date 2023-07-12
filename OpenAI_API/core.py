# Import necessary modules
import openai
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=1)

def create_chat_completion(prompt, model):
    """
    Helper function to call openai.ChatCompletion.create with the correct arguments.
    This function can be used with run_in_executor.
    """
    return openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

async def interact_with_openai(prompt, model):
    """
    Function to interact with the OpenAI API and get a response.
    """
    loop = asyncio.get_event_loop()

    response = await loop.run_in_executor(
        executor, 
        create_chat_completion,
        prompt, 
        model
    )

    reply = response.choices[0].message.content.strip()

    return reply

async def chat_with_openai():
    """
    Function to initiate a chat interaction with the OpenAI models.
    """
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["quit", "exit"]:
            break
        model = "gpt-3.5-turbo"  # The default model
        response = await interact_with_openai(prompt, model)
        print(f"AI: {response}")
