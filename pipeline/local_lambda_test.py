from __future__ import print_function
from boto3.session import Session

import json
import urllib
import boto3
import botocore
import re

# Paste your template here
template = """
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "a sample test 'app' that creates a single SG with 1 SSH rule. This one with global SSH rule",
  "Resources": {
    "sg": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "SSH Security Group",
        "SecurityGroupIngress": {
          "CidrIp": "0.0.0.0/0",
          "FromPort": 22,
          "ToPort": 22,
          "IpProtocol": "tcp"
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "demo1"
          },
          {
            "Key": "LOB",
            "Value": "Finance"
          }
        ]
      }
    }
  }
}
"""



def evaluate_template(template):
    passed = True
    failed_rules = []
    jsonTemplate = json.loads(template)
    #for i in jsonTemplate['Resources']:
    #    print(jsonTemplate['Resources'][i])

    """Main CFT Validation function

    This is where you'll implement all your security, compliance and governance logic to validate the CFT.

    Args:
        template: the CFT template to verify

    Returns:
        pass/fail, list of errors in case of a failure   
    """
    # ---------------------------------------------------
    # --- start implementing your security logic here ---
    # ---------------------------------------------------
    print(json.dumps(jsonTemplate, sort_keys=True, indent=4, separators=(',', ': ')))
   
    return passed, failed_rules

#Local testing - run function
print(evaluate_template(template))