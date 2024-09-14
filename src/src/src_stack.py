from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class SrcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Check if we are using LocalStack
        use_localstack = self.node.try_get_context("use_localstack")

        # Set the endpoint URL for LocalStack
        endpoint_url = "http://localhost:4566" if use_localstack else None

         # Create an S3 bucket with LocalStack endpoint
        bucket = s3.Bucket(self, "TamilMetadataBucket",
                           bucket_name="tamil.metadata-bucket")
