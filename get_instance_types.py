"""
Purpose: Get instance types for a given region and availability zone
Usage:
- python3 get_instance_types.py --region us-east-1 --availability_zone us-east-1a --instance_type t2.micro
- python3 get_instance_types.py --region us-east-1 --availability_zone us-east-1a --instance_type "t2.*"
- python3 get_instance_types.py --region us-east-1 --availability_zone "*" --instance_type g3.4xlarge
"""

import argparse
import boto3

def get_args():
    "Parses arguments"
    parser = argparse.ArgumentParser(description='Get instance types')
    parser.add_argument('--region', help='AWS region')
    parser.add_argument('--availability_zone', help='AWS availability zone')
    parser.add_argument('--instance_type', help='AWS instance type')
    args = parser.parse_args()
    return args
args = get_args()

def get_instance_types(region, location, instance_type):
    "Returns a list of instance types"
    client = boto3.client('ec2', region)
    response = client.describe_instance_type_offerings(
        LocationType='availability-zone',
        Filters=[
            {
                'Name': 'location',
                'Values': [location]
            },
            {
                'Name': 'instance-type',
                'Values': [instance_type]
            }
        ],
    )
    return response['InstanceTypeOfferings']

def main():
    "Calls get_instance_types and returns a list of instance types"
    instance_types = get_instance_types(region=args.region, location=args.availability_zone, instance_type=args.instance_type)
    for instance_type in instance_types:
        print(instance_type['InstanceType'])

if __name__ == '__main__':
    main()