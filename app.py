from aws_cdk import core
from infra.cdk_stack import CDKStack

app = core.App()
CDKStack(app, "my-bucket-stack")
app.synth()