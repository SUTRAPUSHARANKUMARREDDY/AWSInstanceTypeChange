import json
import boto3
import requests
from datetime import datetime
import pytz
import constant

def send_slack_message(slack_webhook_url, slack_message):
  print('>send_slack_message:slack_message:'+slack_message)
  slack_payload = {'text': slack_message}
  print('>send_slack_message:posting message to slack channel')
  response = requests.post(constant.slack_webhook_url, json.dumps(slack_payload))
  response_json = response.text  # convert to json for easy handling
  print('>send_slack_message:response after posting to slack:'+str(response_json))

def change_instance_type():

  notification_message = 'The following EC2 instance type is chanded: \n'
  ec2_info = "Instance Name: " + constant.instancename
  notification_message += ec2_info + '\n'
  ec2_info = ec2_info + "InstanceId: " + constant.instanceid
  notification_message += ec2_info + '\n'
  ec2_info = ec2_info + "from" + constant.oldinstancetype + "To" + constant.newinstancetype
  notification_message += ec2_info + '\n'

  for region in constant.regions:
    client = boto3.client("ec2", region_name=region)

    client.stop_instances(InstanceIds=[constant.instanceid])
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[constant.instanceid])
    client.modify_instance_attribute(InstanceId=constant.instanceid, Attribute='instanceType', Value=constant.newinstancetype)
    client.start_instances(InstanceIds=[constant.instanceid])

  send_slack_message(constant.slack_webhook_url, notification_message) 

def lambda_handler(event, context):
    change_instance_type()
    return {
      'statusCode': 200,
      'body': json.dumps('The Instance type change Process is completed.')
    }