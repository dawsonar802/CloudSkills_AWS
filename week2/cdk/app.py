#!/usr/bin/env python3

from aws_cdk import core as core
from cdk.cdk_stack import CdkStack
import aws_cdk.aws_s3 as s3

class S3(core.Stack):
    def S3Stack(self):
        s3.Bucket(
            bucket_name="cloudskills0019999"
        )

app = core.App()
S3(app, "cdk")

app.synth()
