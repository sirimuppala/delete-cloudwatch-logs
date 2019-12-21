#!/usr/bin/python
#Utility to remove cloudwatch log group with prefix
#Usage : python delete_cloudwatch_logs.py  -l <loggroup-name-prefix> -r <aws-region> -p  <aws-profile-name>
#Sample usage : python delete_cloudwatch_logs.py -l /aws/sagemaker/Endpoints/DEMO-MultiMod -r us-west-2 -p dev

#Sample output
## loggroup_prefix  /aws/lambda/MediaAnalysis
## Found  5  logGroups with prefix  /aws/lambda/MediaAnalysis
## Deleting the log group  /aws/lambda/MediaAnalysis-MediaAnalysisFunction-1ACQX90ZEKJP2
## Deleting the log group  /aws/lambda/MediaAnalysis-MediaAnalysisFunction-I9YR22CP9P0K
## Deleting the log group  /aws/lambda/MediaAnalysis-MediaAnalysisHelperFunction-11H4FGIUZ7PZS
## Deleting the log group  /aws/lambda/MediaAnalysis-MediaAnalysisHelperFunction-1HOEYWCRTFNCB
## Deleting the log group  /aws/lambda/MediaAnalysis-MediaAnalysisHelperFunction-FQ3XSOET2ACG

##########################################################################################################
import boto3
import argparse

def delete_log_group_with_prefix(loggroup_prefix):
    session = boto3.Session(profile_name=aws_profile)
    client = session.client('logs', region_name=aws_region)

    #Get the loggroups starting with the prefix.
    response = client.describe_log_groups(
        logGroupNamePrefix=loggroup_prefix
    )

    logGroups = response['logGroups']
    print('Found ', len(logGroups), ' logGroups with prefix ', loggroup_prefix)

    #Loop through the logGroups and delete each one.
    for logGroup in logGroups:
        print('Deleting the log group ', logGroup['logGroupName'])
        client.delete_log_group(
            logGroupName = logGroup['logGroupName']
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--loggroup-prefix')
    parser.add_argument('-p', '--aws-profile')
    parser.add_argument('-r', '--aws-region')
    args = parser.parse_args()

    aws_region = args.aws_region
    aws_profile = args.aws_profile

    loggroup_prefix = args.loggroup_prefix
    print('loggroup_prefix ', loggroup_prefix)

    delete_log_group_with_prefix(loggroup_prefix)


