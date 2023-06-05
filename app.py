from aws_cdk import core
from cdk.cdk_stack import CDKStack

app = core.App()
CDKStack(app, "my-bucket-stack")
app.synth()