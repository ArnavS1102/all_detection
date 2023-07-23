import boto3
import os

class S3:
    def __init__(self, bucket, file_name):
        self.access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        self.bucket = bucket
        self.file_name = file_name

    def save_file(self, file_path):
        s3 = boto3.client('s3', aws_access_key_id = self.access_key, aws_secret_access_key = self.secret_key)
        s3.upload_file(file_path, self.bucket, self.file_name)
    
    def load_file(self):
        s3 = boto3.client('s3', aws_access_key_id = self.access_key, aws_secret_access_key = self.secret_key)
        response = s3.get_object(Bucket = self.bucket, Key = self.file_name)
        image_data = response['Body'].read()
        return image_data
    
    



    
