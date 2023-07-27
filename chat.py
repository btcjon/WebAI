from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import openai
import argparse
import json
import asyncio
import sys
import io
import re
from bardapi import Bard
from EdgeGPT.src.EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from OpenAI_API.core import interact_with_openai
from concurrent.futures import ThreadPoolExecutor
from tools.file_system_tool import FileSystemTool
from tools.webscraper_tool import WebScraperTool
from tools.website_crawler_tool import WebsiteCrawlerTool
from tools.s3_tool import S3Tool
from llm import LLM
from lang_chain import LangChain
from tool_chain import ToolChain
from command_parser import CommandParser
from memory_manager import ShortTermMemory

from collections import deque

# Initialize LangChain with the list of LLMs
langchain = LangChain([Bard, GPT3, GPT4])

# Initialize the memory with a size of 3800 tokens
memory = ShortTermMemory(3800)

async def main():
    user_id = 1  # Replace with the actual user ID
    session_id = 0  # Initialize session ID
    while True:
        prompt = input("You: ")
        # Increment the session ID for each new conversation
        session_id += 1
        # Add the user's message to the memory
        memory.add_message(prompt)
        print("Current Memory: ", memory.get_messages())
        response = await langchain.process(prompt, 'Bard', user_id, session_id)
        print("Bot: ", response)

if __name__ == "__main__":
    asyncio.run(main())
