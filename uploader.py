import boto3
from io import BytesIO
import time

class S3Uploader:
    def __init__(self, config):
        self.s3_client = boto3.client('s3')
        self.bucket_name = config.config_data.get('s3_bucket')
        self.retry_queue = []

    def upload(self, file_data):
        filename = f"screenshot_{int(time.time())}.jpg"
        
        # Ensure file_data is a BytesIO object
        if not isinstance(file_data, BytesIO):
            file_data = BytesIO(file_data)
        
        # Reset the file pointer to the beginning of the stream
        file_data.seek(0)
        
        try:
            self.s3_client.upload_fileobj(file_data, self.bucket_name, filename)
            print(f"Uploaded {filename} successfully.")
        except Exception as e:
            print(f"Upload failed: {str(e)}, adding to retry queue")
            self.queue_file_for_retry(file_data)

    def queue_file_for_retry(self, file_data):
        # Logic to add file to retry queue
        self.retry_queue.append(file_data)

    def retry_upload(self):
        # Retry logic when internet connection is restored
        for file_data in self.retry_queue:
            try:
                self.upload(file_data)
                self.retry_queue.remove(file_data)
            except Exception as e:
                print(f"Retry failed: {str(e)}, will try again later")
