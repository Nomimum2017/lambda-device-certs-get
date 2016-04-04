# coding: utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

import boto3
import uuid

def lambda_handler(event, context):

    deviceId = event['params']['deviceId']

    dynamodb = boto3.resource('dynamodb')
    certTable = dynamodb.Table('device-certs')

    getCerts = certTable.get_item(
        Key={
            'deviceId': deviceId
        }
    )
    print("getCerts output: ", getCerts['ResponseMetadata'])

    return ("{ \"deviceCerts\": {" +
        "\"deviceId\": " + getCerts['Item']['deviceId'] + "," +
        "\"certificatePem\": " + getCerts['Item']['certificatePem'] + "," +
        "\"publicKey\": " + getCerts['Item']['publicKey'] + "," +
        "\"privateKey\": " + getCerts['Item']['privateKey'] +
    "}}")