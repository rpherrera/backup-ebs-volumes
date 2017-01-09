#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# This function looks at *all* snapshots that have a "DeleteOn" tag containing
# the current day formatted as YYYY-MM-DD. This function should be run at least
# daily.
#
# Taken from:
# https://serverlesscode.com/post/lambda-schedule-ebs-snapshot-backups-2/
#

import boto3
import re
import datetime
import os

ec = boto3.client('ec2')
iam = boto3.client('iam')
account_ids = os.environ['AWS_ACCOUNT_IDS'].split(',')

delete_on = datetime.date.today().strftime('%Y-%m-%d')
filters = [
    {'Name': 'tag-key', 'Values': ['DeleteOn']},
    {'Name': 'tag-value', 'Values': [delete_on]},
]
snapshot_response = ec.describe_snapshots(OwnerIds=account_ids, Filters=filters)

for snap in snapshot_response['Snapshots']:
    print "Deleting snapshot %s" % snap['SnapshotId']
    ec.delete_snapshot(SnapshotId=snap['SnapshotId'])
