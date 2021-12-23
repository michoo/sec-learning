# aws


## Installation

sudo apt-get install awscli
aws --version
aws configure

key=AKIATAAH6Q3WM3U5ORWT
secret=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
json

~/.aws/config
~/.aws/credentials 

pour cleaner rm -v ~/.aws/config ~/.aws/credentials


## flag

get whoami
aws sts get-caller-identity 

get a specific secret
aws secretsmanager get-secret-value --secret-id hf-aws-beginner-challenge2-secret 

copy files
aws s3 cp s3://hf-aws-beginner-challenge3-bucket-206175110892 myDir --recursive

dump data
aws dynamodb scan --table-name hf-aws-beginner-challenge4-table > dump.json

assume role
export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \
$(aws sts assume-role \
--role-arn arn:aws:iam::206175110892:role/hf-aws-beginner-challenge5-role \
--role-session-name MySessionName \
--query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
--output text))
run commande
aws ssm get-parameter --name hf-aws-beginner-challenge5-parameter

authsignature
pip install aws-requests-auth
signature/request.py

lambda
pip install boto3 
lambda/lambda.py

docker pull and run
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 206175110892.dkr.ecr.us-east-1.amazonaws.com/hf-aws-beginner-challenge8-repository
docker pull 206175110892.dkr.ecr.us-east-1.amazonaws.com/hf-aws-beginner-challenge8-repository


logs
aws logs describe-log-streams --log-group-name hf-aws-beginner-challenge9-log-group

some-log-stream

aws logs get-log-events --log-group-name hf-aws-beginner-challenge9-log-group --log-stream-name some-log-stream --limit 10

