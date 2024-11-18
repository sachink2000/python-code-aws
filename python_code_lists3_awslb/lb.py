import boto3
client = boto3.client('elbv2')
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_albs():
    try:
        # Initialize a client for the Elastic Load Balancing (ELBv2) service
        elb_client = boto3.client('elbv2')

        # Call to describe the load balancers
        response = elb_client.describe_load_balancers()

        # Extract the list of ALBs
        load_balancers = response['LoadBalancers']

        if not load_balancers:
            print("No Application Load Balancers (ALBs) found.")
        else:
            print("List of Application Load Balancers (ALBs):")
            for alb in load_balancers:
                alb_name = alb['LoadBalancerName']
                alb_arn = alb['LoadBalancerArn']
                alb_type = alb['Type']
                dns_name = alb['DNSName']
                state = alb['State']['Code']
                created_time = alb['CreatedTime']

                print(f"ALB Name: {alb_name}")
                print(f"ARN: {alb_arn}")
                print(f"Type: {alb_type}")
                print(f"DNS Name: {dns_name}")
                print(f"State: {state}")
                print(f"Created Time: {created_time}")
                print("-" * 60)

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list ALBs
list_albs()
