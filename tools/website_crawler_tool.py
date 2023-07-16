import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebsiteCrawlerTool:
    def __init__(self, name):
        self.name = name
        self.visited = set()  # a set to hold the visited URLs

    commands = {
        "crawl": ("Crawls a website and saves a list of all URLs to a file. Usage: crawl <url>", "crawl_website")
    }

    def crawl_website(self, url):
        # Make sure the url ends with a slash
        if not url.endswith('/'):
            url += '/'
        self.visited.clear()
        self._crawl_page(url, url)

        # Get the output file
        output_file = self._get_output_file(url)

        # Save the URLs to the output file
        with open(output_file, 'w') as f:
            for visited_url in self.visited:
                f.write(visited_url + '\n')

        # Return the path to the output file
        return output_file

    def _crawl_page(self, url, base_url):
        if url not in self.visited and url.startswith(base_url):
            print(f"Crawling: {url}")
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.findAll('a'):
                    href = link.get('href')
                    if href:
                        # Join the URL with the base URL, in case of relative links
                        full_url = urljoin(url, href)
                        # Only crawl pages within the same directory
                        if full_url.startswith(base_url):
                            self.visited.add(full_url)
                            # Recursively crawl the linked page
                            self._crawl_page(full_url, base_url)
            except requests.exceptions.RequestException as e:
                print(e)

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
        filename = f"{domain}_{path}_sitemap.txt"

        # Return the full path to the output file
        return os.path.join('workspace', 'sitemaps', filename)
