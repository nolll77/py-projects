# code exported from "organize-s3-objects4-export.ipynb" file
# Clean the syntax added by the export (ie the <# %%> and spaces added between lines)
# Add a lambda line 10
# resyntaxed lines after line 10
# then save this file as a Python format file (cmd + S)

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