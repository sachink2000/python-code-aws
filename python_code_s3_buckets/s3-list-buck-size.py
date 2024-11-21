import boto3

# Initialize a session using Amazon S3
session = boto3.Session(
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='your_region'
)

# Initialize S3 resource
s3 = session.resource('s3')

# Function to calculate the size of a bucket
def get_bucket_size(bucket_name):
    total_size = 0
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.all():
        total_size += obj.size
    return total_size

# List all buckets and their sizes
def list_buckets_and_sizes():
    s3_client = session.client('s3')
    buckets = s3_client.list_buckets()
    
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        bucket_size = get_bucket_size(bucket_name)
        print(f"Bucket: {bucket_name}, Size: {bucket_size / (1024**2):.2f} MB")

if __name__ == "__main__":
    list_buckets_and_sizes()
