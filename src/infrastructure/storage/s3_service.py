import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError
from application.storage_service import StorageService

class S3StorageService(StorageService):
    def __init__(self):
        self.bucket_name = os.environ['S3_BUCKET']
        self.client = boto3.client(
            's3',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            region_name=os.environ.get('AWS_REGION', 'us-east-1')
        )

    def upload_file(self, file, object_key: str) -> str:
        try:
            self.client.upload_fileobj(file, self.bucket_name, object_key)
            url = f"https://{self.bucket_name}.s3.amazonaws.com/{object_key}"
            return url
        except (BotoCoreError, ClientError) as e:
            raise Exception(f"Failed to upload to S3: {e}")
