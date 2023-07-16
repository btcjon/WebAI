import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlsplit

class WebScraperTool:
    def __init__(self, name):
        self.name = name
        self.workspace_dir = "workspace"
        self.scraped_dir = os.path.join(self.workspace_dir, "scraped")
        self.urls_file = os.path.join(self.workspace_dir, "urls.txt")
        self.commands = {
            "scrape": ("Scrapes a webpage and saves the content to a file. Usage: scrape <url>", "scrape"),
            "scrape_file": ("Scrapes all webpages listed in a file. Usage: scrape_file <file>", "scrape_file")
        }

        # Create the workspace and scraped directories if they don't exist
        os.makedirs(self.workspace_dir, exist_ok=True)
        os.makedirs(self.scraped_dir, exist_ok=True)

    def scrape(self, url):
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the text from the page
        text = soup.get_text()

        # Get the output file
        output_file = self._get_output_file(url)

        # Save the text to the output file
        with open(output_file, 'w') as f:
            f.write(text)

        # Return the path to the output file
        return output_file

    def scrape_file(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            url = line.strip()  # Remove any leading/trailing whitespace or newlines
            # Check if the line is a valid URL
            try:
                result = urlsplit(url)
                if all([result.scheme, result.netloc]):
                    self.scrape(url)
                else:
                    print(f"Invalid URL: {url}")
            except Exception as e:
                print(f"Error occurred while processing URL: {url}. Error: {e}")

    def _get_output_file(self, url):
        # Parse the URL to get the domain and path
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path

        # Remove any leading or trailing slashes from the path
        path = path.strip('/')

        # Replace any remaining slashes in the path with underscores
        path = path.replace('/', '_')

        # Combine the domain and path to create the filename
        filename = f"{domain}_{path}.txt"

        # Return the full path to the output file
        return os.path.join(self.scraped_dir, filename)
