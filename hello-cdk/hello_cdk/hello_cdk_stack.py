from aws_cdk import (
    aws_s3 as s3,
    core as cdk
)


class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct,
                 construct_id: str,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            scope=self,
            id="MyFirstBucket",
            public_read_access=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            versioned=True)
