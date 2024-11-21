import boto3
client = boto3.client('ec2')
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_ec2_instances():
    try:
        # Initialize an EC2 client
        ec2_client = boto3.client('ec2')

        # Retrieve all EC2 instances
        response = ec2_client.describe_instances()

        # Extract the instances details from the response
        instances = response['Reservations']
        
        if not instances:
            print("No EC2 instances found.")
        else:
            print("List of EC2 Instances:")
            for reservation in instances:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    instance_type = instance['InstanceType']
                    state = instance['State']['Name']
                    public_ip = instance.get('PublicIpAddress', 'N/A')
                    private_ip = instance.get('PrivateIpAddress', 'N/A')
                    launch_time = instance['LaunchTime']

                    print(f"Instance ID: {instance_id}")
                    print(f"Instance Type: {instance_type}")
                    print(f"State: {state}")
                    print(f"Public IP: {public_ip}")
                    print(f"Private IP: {private_ip}")
                    print(f"Launch Time: {launch_time}")
                    print("-" * 60)

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list EC2 instances
list_ec2_instances()
