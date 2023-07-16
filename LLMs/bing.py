import json
import logging
from EdgeGPT.src.EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from llm import LLM
from .llm_capabilities import bing_capabilities

# Configure logging
logging.basicConfig(level=logging.INFO)

async def chat_with_bing(prompt):
    try:
        logging.info("Starting chat_with_bing function")
        
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        logging.info("Loaded cookies from cookies.json")
        
        bing = await Chatbot.create(cookies=cookies)
        logging.info("Created Chatbot instance")
        
        response = await bing.ask(prompt, conversation_style=ConversationStyle.creative)
        logging.info("Received response from Bing")
        
        message = response['item']['messages'][-1]['text']  # Extract the desired message
        logging.info("Extracted message from response")
        
        return message
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

bing_llm = LLM(chat_with_bing, 'Bing', 'Bing', bing_capabilities)
