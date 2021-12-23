import boto3, json

lambda_client = boto3.client('lambda')

test_event = dict()

response = lambda_client.invoke(
  FunctionName='hf-aws-beginner-challenge7-lambda',
  Payload=json.dumps(test_event),
)

print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))