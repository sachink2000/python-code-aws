import boto3
from datetime import datetime

# Initialize a session using Amazon EC2
session = boto3.Session(
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='your_region'
)

# Initialize EC2 resource
ec2 = session.resource('ec2')

# Specify the instance IDs
instance_ids = ['i-0123456789abcdef0', 'i-0abcdef1234567890']  # Replace with your instance IDs

def start_instances():
    ec2.instances.filter(InstanceIds=instance_ids).start()
    print(f"{datetime.now()}: Instances started: {instance_ids}")

def stop_instances():
    ec2.instances.filter(InstanceIds=instance_ids).stop()
    print(f"{datetime.now()}: Instances stopped: {instance_ids}")

if __name__ == "__main__":
    # Get the current hour
    current_hour = datetime.now().hour

    # Start instances at 8 AM and stop at 8 PM
    if current_hour == 8:
        start_instances()
    elif current_hour == 20:
        stop_instances()
