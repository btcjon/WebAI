import os
from tools.s3_tool import S3Tool

class FileSystemTool:
    def __init__(self, name, s3_tool):
        self.name = name
        self.s3_tool = s3_tool
        self.commands = {
            "read": ("Reads the content of a file. Usage: read <filename>", self.read_file),
            "write": ("Writes content to a file. Usage: write <filename> <content>", self.write_file),
            "read_and_prompt": ("Reads a file and returns its contents as a string. Usage: read_and_prompt <filename>", self.read_and_prompt),
        }

    def read_file(self, filename):
        # If file does not exist locally, try to download it from S3
        if not os.path.exists(filename):
            self.s3_tool.download_file(filename)

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)  
                return content
        else:
            return f"Error: {filename} does not exist."

    def write_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

        # Check the size of the file
        file_size = os.path.getsize(filename)

        # If the file size is greater than 5MB, move it to the S3 bucket
        if file_size > 5 * 1024 * 1024:
            self.s3_tool.upload_file(filename)
            os.remove(filename)

    def read_and_prompt(self, filename):
        # If file does not exist locally, try to download it from S3
        if not os.path.exists(filename):
            self.s3_tool.download_file(filename)

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        else:
            return f"Error: {filename} does not exist."
