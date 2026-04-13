import aws_cdk as cdk
from cdk_stack import EksGitopsPlatformStack

app = cdk.App()

EksGitopsPlatformStack(
    app, "EksGitopsPlatformStack",
    env=cdk.Environment(
        account="585707316406",
        region="ap-south-1"
    )
)

app.synth()