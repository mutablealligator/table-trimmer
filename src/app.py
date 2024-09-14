#!/usr/bin/env python3
import os
import aws_cdk as cdk
from src.src_stack import SrcStack

app = cdk.App()

use_localstack = app.node.try_get_context("use_localstack") == "true"

if use_localstack:
    os.environ['CDK_DEFAULT_ACCOUNT'] = '123456789012'
    os.environ['CDK_DEFAULT_REGION'] = 'us-east-1'
    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_ENDPOINT_URL'] = 'http://localhost:4566'  # Add this line

env = cdk.Environment(
    account=os.environ.get('CDK_DEFAULT_ACCOUNT', '123456789012'),
    region=os.environ.get('CDK_DEFAULT_REGION', 'us-east-1')
)

print(f"Environment: {env}")
print(f"Using LocalStack: {use_localstack}")

SrcStack(app, "SrcStack", env=env, use_localstack=use_localstack)

app.synth()