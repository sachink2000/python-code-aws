import boto3
s3 = boto3.resource('s3')
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        # Initialize a session using AWS credentials
        s3_client = boto3.client('s3')

        # Call to list all buckets
        response = s3_client.list_buckets()

        # Extract bucket names
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        if not bucket_names:
            print("No S3 buckets found.")
        else:
            print("List of S3 Buckets:")
            for bucket in bucket_names:
                print(f"- {bucket}")

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list buckets
list_s3_buckets()
