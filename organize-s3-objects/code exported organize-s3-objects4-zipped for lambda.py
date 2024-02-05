# add the py code into a zip file, do that manually via the finder
# In the UI, create a s3 bucket and then upload the zip file in it
# So Lambda can pull it


# Next step: create an IAM-Role in aws that Lambda will use to trigger the code (role: AWS service)
# policies = s3FullAccess and LambdaBasicExecutionRole

# then from the aws Lambda dashboard create a Function in which we use the existing role created previously

# Then add a trigger to the Lambda function
# from Lambda dashboard > Function > Add trigger
# source = s3
# Event type: PUT

# Upload Python Code in the Lambda Function
# from Lambda dashboard > Function > Upload from
# look for the zip object's URL in the dedicated s3 bucket for the zip file

# Update the Handler Settings and Create a Test Event
# From the 'Code' tab > Runtime settings > Edit
# Handler field > put the name of the py with suffix .lambda_handler

# Then "Test" tab > Create new event > Save > then click test

# Test wether the Lambda Function is working
# Upload manually random files in the s3
# Those files goes directly in the good "Today's floder"
# Because when we've set up the Lambda function in the aws Lambda dashboard it's created a kind of automation

import boto3
from datetime import datetime

today = datetime.today()
todays_date = today.strftime("%Y%m%d")

def lambda_handler(event, context):

    s3_client = boto3.client('s3')

    bucket_name = "nol-organize-s3-objects"

    list_objects_response = s3_client.list_objects_v2(
        Bucket=bucket_name
    )

    get_contents = list_objects_response.get("Contents")

    get_all_s3_object_and_folder_names = []

    for i in get_contents:
        s3_object_name = i.get("Key")
        
        get_all_s3_object_and_folder_names.append(s3_object_name)

    directory_name = todays_date + "/"

    if directory_name not in get_all_s3_object_and_folder_names:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=(directory_name)
        )

    for i in get_contents:
        object_creation_date = i.get("LastModified").strftime("%Y%m%d") + "/"
        object_name = i.get("Key")
        
        if object_creation_date == directory_name and "/" not in object_name:
            s3_client.copy_object(
                Bucket=bucket_name,
                CopySource=bucket_name+"/"+object_name,
                Key=directory_name+object_name
            )
            
            s3_client.delete_object(
                Bucket=bucket_name,
                Key=object_name
            )