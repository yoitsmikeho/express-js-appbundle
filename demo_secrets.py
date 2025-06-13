# demo_secrets.py

import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Simulated AWS credentials for GitHub Advanced Security demo
aws_access_key_id = "AKIA1234567890FAKE"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
github_token="ghp_ddM8q3nuSCvZjVhMcs3zcOF2E1fJXF4B5iBE"
gitlab_token="glpat-jhbdfkjbdfb"

def list_s3_buckets():
    try:
        print("Initializing S3 client...")
        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        response = s3.list_buckets()
        print("Buckets found:")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")
    except NoCredentialsError:
        print("Credentials not found.")
    except ClientError as e:
        print(f"AWS Client Error: {e}")

if __name__ == "__main__":
    list_s3_buckets()



