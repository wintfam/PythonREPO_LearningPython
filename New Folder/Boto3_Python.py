#BOTO3_PYTHON

import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.bucket("luits3_tech")
response = bucket.create(
    ACL='public-read'
    )
 

print(response)