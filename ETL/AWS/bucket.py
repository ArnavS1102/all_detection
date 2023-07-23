import boto3
import os

class Bucket:

    def __init__(self, bucket_name):
        self.access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket = bucket_name)

