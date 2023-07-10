# color_format.py
from colorama import Fore, Style, init

init()

def format_title(text):
    return Fore.GREEN + 'Title: ' + Fore.RESET + text

def format_snippet(text):
    return Fore.BLUE + 'Snippet: ' + Fore.RESET + text

def format_url(text):
    return Fore.MAGENTA + 'URL: ' + Fore.RESET + text

# Then, in your main file:
from color_format import format_title, format_snippet, format_url
