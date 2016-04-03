# coding: utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

import boto3
import uuid

def lambda_handler(event, context):

    deviceId = event['body']['deviceId']

    dynamodb = boto3.resource('dynamodb')
    certTable = dynamodb.Table('device-certs')

    getCerts = certTable.get_item(
        Key={
            'deviceId': deviceId
        }
    )
    print("getCerts output: ", getCerts['ResponseMetadata'])

    return {"deviceCerts": {
        "deviceId": getCerts['deviceId'],
        "certificatePem": getCerts['deviceId'],
        "PublicKey": getCerts['PublicKey'],
        "PrivateKey": getCerts['PrivateKey']
    }}