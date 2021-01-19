from copy import Error

import boto3
from config import S3_BUCKET_NAME


def upload_file(file_name, object_name):
    if not S3_BUCKET_NAME:
        raise Error("cannot upload to S3, S3_BUCKET_NAME not specified")
    print(f"Uploading to S3 bucket {S3_BUCKET_NAME}")
    s3 = boto3.client('s3')
    with open(file_name, "rb") as f:
        s3.upload_fileobj(f, S3_BUCKET_NAME, object_name)

