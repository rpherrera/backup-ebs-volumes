#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#
# This example was taken from:
# https://serverlesscode.com/post/lambda-schedule-ebs-snapshot-backups/
#

import boto3

if __name__ == '__main__':
    ec = boto3.client('ec2')
    reservations = ec.describe_instances(
            Filters=[
                {'Name': 'tag-key', 'Values': ['backup', 'Backup']},
            ]
        )['Reservations']

    instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])

    for instance in instances:
        for dev in instance['BlockDeviceMappings']:
            if dev.get('Ebs', None) is None:
                # skip non-EBS volumes
                continue
            vol_id = dev['Ebs']['VolumeId']
            print "Found EBS volume %s on instance %s" % (
                vol_id, instance['InstanceId'])

            ec.create_snapshot(
                VolumeId=vol_id,
            )
