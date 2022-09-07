#BOTO3_PYTHON

import boto3
aws_resource=boto3.resorce("s3")
bucket=aws_resource.Bucket("totaltechnology")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },
    
)    
 

print(response
)