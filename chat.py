from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import argparse
import json
import asyncio
from BardAPI.bardapi.core import Bard
from EdgeGPT.src.EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    parser = argparse.ArgumentParser(description='Interact with Bard and Bing APIs.')
    parser.add_argument('--bard', help='Send a request to the Bard API.')
    parser.add_argument('--bing', help='Send a request to the Bing API.')
    args = parser.parse_args()

    if args.bard:
        bard = Bard()  # Bard doesn't require any parameters in the constructor
        result = bard.get_answer(args.bard)  # get_answer is the method to get the response from Bard
        print(result)

    if args.bing:
        # Load cookies from cookies.json
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)

        bing = await Chatbot.create(cookies=cookies)  # Bing requires cookies in the constructor
        result = await bing.ask(args.bing, conversation_style=ConversationStyle.creative)  # ask is the method to get the response from Bing
        print(result)
        await bing.close()

if __name__ == "__main__":
    asyncio.run(main())
