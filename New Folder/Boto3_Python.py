#BOTO3_PYTHON

import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("luit-s3tech-tony")

response = bucket.create(
    ACL='public-read',
    )
    
    
print(response)