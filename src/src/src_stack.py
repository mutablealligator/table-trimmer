# from aws_cdk import (
#     Duration,
#     Stack,
#     aws_s3 as s3,
#     Environment,
# )
# from constructs import Construct

# class SrcStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, use_localstack: bool = False, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         if use_localstack:
#             print("Configuring for LocalStack")
#             # LocalStack specific configurations
#             s3.Bucket.physical_name_prefix = 'localstack-'
#             # Override the S3 endpoint to use LocalStack
#             self.node.set_context("@aws-cdk/aws-s3:endpoint", "http://localhost:4566")

#         # Create an S3 bucket
#         bucket = s3.Bucket(self, "TamilMetadataBucket",
#                            bucket_name="tamil.metadata-bucket")
        
#         print(f"Bucket created: {bucket.bucket_name}")

import aws_cdk as cdk
from constructs import Construct
import boto3
import os

class SrcStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, use_localstack: bool, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if use_localstack:
            print("Configuring for LocalStack")
            endpoint_url = os.environ.get('AWS_ENDPOINT_URL', 'http://localhost:4566')
            s3 = boto3.client('s3', 
                endpoint_url=endpoint_url,
                aws_access_key_id='test',
                aws_secret_access_key='test',
                region_name='us-east-1')
        else:
            s3 = boto3.client('s3')

        # Use the s3 client to create resources
        bucket_name = f"my-bucket-{self.account}-{self.region}"
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket created: {bucket_name}")

        # Add other resources and configurations as needed