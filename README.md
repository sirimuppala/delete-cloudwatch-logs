# Bulk deletion of cloudwatch loggroups
Python utility to delete cloudwatch logs in bulk based on log group name prefix.  Useful when you want to clean up cloudwatch logs that start to accumulate as you use various services in your dev/QA AWS accounts.

**Sample Usage** 

python delete_cloudwatch_logs.py -l /aws/sagemaker/lambda/Media- -r us-west-2 -p dev

**Example**

python delete_cloudwatch_logs.py  -l /aws/sagemaker/Endpoints/Recs-Multi  -r us-west-2 -p  dev -l /aws/sagemaker/Endpoints/Recs-Multi

Found  9  logGroups with prefix  /aws/sagemaker/Endpoints/Recs-Multi
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-17-37-05
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-18-20-56
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-18-36-10
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-19-06-35
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-19-18-00
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-20-37-18
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-20-49-00
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-21-08-23
Deleting the log group  /aws/sagemaker/Endpoints/Recs-MultiModelEndpoint-2019-11-12-21-52-14




