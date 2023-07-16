import boto3
from botocore.exceptions import NoCredentialsError

class S3Tool:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.name = "S3 Tool" 
        self.commands = {
            'upload': ('Upload a file to the S3 bucket', self.upload_file),
            'download': ('Download a file from the S3 bucket', self.download_file),
            'list': ('List all files in the S3 bucket', self.list_files),
            'delete': ('Delete a file from the S3 bucket', self.delete_file),
        }

    def upload_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_file(self, object_name, file_name=None):
        if file_name is None:
            file_name = object_name
        self.s3.download_file(self.bucket_name, object_name, file_name)

    def list_files(self):
        response = self.s3.list_objects(Bucket=self.bucket_name)
        if 'Contents' in response:
            for file in response['Contents']:
                print(file['Key'])
        else:
            print("No files in the bucket.")


    def delete_file(self, object_name):
        self.s3.delete_object(Bucket=self.bucket_name, Key=object_name)
