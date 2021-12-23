import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth

# let's talk to our AWS Elasticsearch cluster
auth = AWSRequestsAuth(aws_access_key='AKIATAAH6Q3WM3U5ORWT',
                       aws_secret_access_key='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',
                       aws_host='dqf7ti8g66.execute-api.us-east-1.amazonaws.com',
                       aws_region='us-east-1',
                       aws_service='execute-api')

response = requests.get('https://dqf7ti8g66.execute-api.us-east-1.amazonaws.com/api/',
                        auth=auth)
print(response.content)