## App Overview

This app performs various tasks on behalf of the user.
It consists of many code-based apps ("tools") utilized within a conversational chat via CLI interacting with large language models.  The app consists of a full artificial intelegence framework.  It attempts to use leverage code-based apps where llms lack proficiency and leverage llms for their unique capabilities.

The tools, features and framework can be accessed directly by the user or by the llm as needed.

## Modularity

All compponents of the app are designed to be independent and modular.


1. Introduction
LangChain is a Python application designed to integrate various Language Learning Models (LLMs) into a single interface. It allows users to interact with models like Bard, Bing, and OpenAI GPT-3 using a unified CLI. Additionally there are many useful tools that user or LLMs can interact with to accomplish many tasks.

## System Architecture and Modules

LangChain employs a simple but effective architecture composed of several parts:

LangChain Framework: This is the backbone of the application for the llm parts of the system. It orchestrates the interactions between the user and the various LLMs.

LLMs: These are the language models that the application can interact with. Each LLM has a dedicated function that handles the interaction with its corresponding API.

Tools: code based tools that either user or LLMs can interct with to accomplish tasks.

## Functionality
The application provides a command-line interface for interacting with the various LLMs. Using command-line flags, users can choose which LLM to use for a particular session, otherwise system defaults to a certain llm.


## Usage
Users interact with the application through a command-line interface. They can specify which LLM to use with command-line flags (e.g., --bing for Bing, --bard for Bard). To send a request to an LLM, users simply type their query into the command line.

## Memory Design (current work-in-progress)

Short-Term Memory (Buffer Window): This part of the memory will hold the last N messages in the ongoing conversation. It's typically implemented as a queue or list data structure that can efficiently add new messages and remove old ones when the limit (N) is reached. Short-term memory helps the model to remember and respond to immediate context in the conversation.

Long-Term Memory (Supabase Database): This will be a Supabase database that stores past conversations. Each record in the database will include a user ID, session ID, timestamp, user message, and AI response. This allows the retrieval of past interactions for a user or a particular session, which is useful for maintaining context across multiple sessions and providing a personalized user experience. The user can access historical data using the user_id and session_id. We will have functions to store and retrieve data from this database.

Vector Storage (Pinecone): This is used for efficient storage and retrieval of memory. For each significant entity or concept, we'll generate a vector representation and store it in Pinecone. When we need to retrieve information, we can generate a vector for the current context and use it to retrieve the most similar vectors (and their associated information) from Pinecone. This can be especially helpful when dealing with large datasets or complex concepts.

Entity Summary Memory: This can be used to store summarized information about different entities that the AI has interacted with. This can help the AI provide accurate and relevant responses when those entities are mentioned in future interactions.


## Improvements to be made
- add conversation memory
- add vector storage
- llm tool ineraction within conversation
- google search tool
- youtube tool (search with filter, transcription scrape)
- document tool (take urls of any file type and save locally for processing txt,csv,pdf-to-text)
- add ways for user to describe task and llm picks the tool to use
- define tool creation process
- add tool usage process so llm knows how to use tools
- automatic tool creation 
- ability to read its own code and edit code
- google doc tool
- google sheet tool
- twitter tool
- define agents from llm (define MANY as sub-set of llm with thier own system message and directives)
- add system messages for agents 
- add file ingestion
- chrome extension (for browser interactions)
- add supabase
- improve scraper

## Misc. Done tasks
- app should default to an llm if no flag used
- add webscraper tool
- add crawl and sitemap tool
- add file storage (5MB+ files to s3 bucket)

## File Summaries (to be updated by AI regularly)

chat.py: This script defines a Chat class that represents a chat session. It includes methods for adding messages to the chat and retrieving all messages from the chat. Each message is a dictionary containing the sender and the content of the message.

lang_chain.py: This file defines the LangChain class that orchestrates the interactions between the user and the various Language Learning Models (LLMs). The process method in the LangChain class takes a prompt and a model_name, and then sends the prompt to the corresponding LLM for processing.

llm.py: This file defines an LLM class that represents a language learning model in the system. Each LLM has properties like a function to process prompts, a name to identify the LLM, a model_name used in the LangChain class, and capabilities.

openai.py: This file defines a function for interacting with the OpenAI GPT-3 model and creates an LLM instance representing the OpenAI model. It sends a chat message to the OpenAI API and returns the response.

bing.py: This file defines a function for interacting with the Bing model and creates an LLM instance representing the Bing model. It sends a chat message to the Bing API and returns the response.

bard.py: This file defines a function for interacting with the Bard model and creates an LLM instance representing the Bard model. It sends a chat message to the Bard API and returns the response.

LLMs/llm_capabilities.py: This file likely defines the capabilities of the different LLMs.

tool_chain.py: This script defines a ToolChain class that represents a collection of tools. It provides methods to add a tool to the collection and to retrieve all tools from the collection.

file_system_tool.py: This script defines a FileSystemTool class that provides an interface to interact with a file system. It includes methods for listing all files in a base directory and reading the contents of a specified file.