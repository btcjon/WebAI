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

from collections import deque

class ShortTermMemory:
    def __init__(self, size):
        self.size = size
        self.memory = deque(maxlen=size)

    def add_message(self, message):
        self.memory.append(message)

    def get_messages(self):
        return list(self.memory)

import logging  # import logging module

logging.basicConfig(level=logging.INFO)  # configure logging

executor = ThreadPoolExecutor(max_workers=5)

# Path to the configuration file
CONFIG_FILE = "config.txt"

def get_default_llm():
    try:
        with open(CONFIG_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        # If the file does not exist, default to Bard
        return 'Bard'

def set_default_llm(llm):
    with open(CONFIG_FILE, 'w') as file:
        file.write(llm)

async def main():
    parser = argparse.ArgumentParser(description='Interact with Bard, Bing, and OpenAI APIs.')
    parser.add_argument('--bard', help='Send a request to the Bard API.', action='store_true')
    parser.add_argument('--bing', help='Send a request to the Bing API.', action='store_true')
    parser.add_argument('--openai', help='Send a request to the OpenAI API with gpt-3.5-turbo.', action='store_true')
    parser.add_argument('--openai16k', help='Send a request to the OpenAI API with gpt-3.5-turbo-16k.', action='store_true')
    parser.add_argument('--gpt4', help='Send a request to the OpenAI API with gpt-4.', action='store_true')
    parser.add_argument('--set-default', help='Set the default model', type=str)
    args = parser.parse_args()

    # If the --set-default flag is used, update the default LLM
    if args.set_default:
        set_default_llm(args.set_default)

    # Get the default LLM
    default_llm = get_default_llm()

    # Here you should import your LLMs
    from LLMs.bard import bard_llm
    from LLMs.bing import bing_llm
    from LLMs.openai import openai_llm_turbo, openai_llm_turbo_16k, openai_llm_4

    langchain = LangChain([bard_llm, bing_llm, openai_llm_turbo, openai_llm_turbo_16k, openai_llm_4])

    s3_tool = S3Tool('webaistorage')  # Create S3Tool instance
    file_tool = FileSystemTool("File Tool", s3_tool)  # Pass S3Tool instance to FileSystemTool
    webscraper_tool = WebScraperTool("Web Scraper")
    website_crawler_tool = WebsiteCrawlerTool("Website Crawler")
    
    toolchain = ToolChain([file_tool, webscraper_tool, website_crawler_tool, s3_tool])  

    # Initialize the CommandParser
    command_parser = CommandParser(toolchain)

    # Instantiate the ShortTermMemory class
    stm = ShortTermMemory(5)

    while True:
        prompt = input("You: ")
        if prompt.lower() in ["quit", "exit"]:
            break

        # Add the user's input to the memory
        stm.add_message("You: " + prompt)
        print("Current Memory: ", stm.get_messages())  # Print the current state of the memory

        # Check if the prompt is a command
        if prompt.lower().startswith("!"):
            if prompt.lower() == "!help":
                CommandParser.list_commands(toolchain)
            else:
                prompt = command_parser.parse(prompt[1:])

        if prompt is not None:
            # Capture the standard output
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout

            if args.bard or (default_llm == 'Bard'):
                response = await langchain.process(prompt, 'Bard')
            if args.bing or (default_llm == 'Bing'):
                response = await langchain.process(prompt, 'Bing')
            if args.openai or (default_llm == 'gpt-3.5-turbo'):
                response = await langchain.process(prompt, 'gpt-3.5-turbo')
            if args.openai16k or (default_llm == 'gpt-3.5-turbo-16k'):
                response = await langchain.process(prompt, 'gpt-3.5-turbo-16k')
            if args.gpt4 or (default_llm == 'gpt-4'):
                response = await langchain.process(prompt, 'gpt-4')

            # Get the printed response
            printed_response = new_stdout.getvalue().strip()
            sys.stdout = old_stdout

            # Add the printed response to the memory
            if printed_response:
                # Remove escape characters and format the response
                formatted_response = re.sub(r'\\n', '\n', printed_response)
                formatted_response = re.sub(r'\\\'', '\'', formatted_response)
                formatted_response = re.sub(r'\\\"', '\"', formatted_response)
                stm.add_message("Bot: " + formatted_response)
                print("Current Memory: ", stm.get_messages())  # Print the current state of the memory

if __name__ == "__main__":
    asyncio.run(main())