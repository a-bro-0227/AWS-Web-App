
# Welcome to your CDK Python project!

This is an example and step-by-step instructions on how to deploy a simple AWS stack using GitHub Actions. In this example, we'll deploy a basic AWS CloudFormation stack. Here's what you need to do:

*# TODO: add more headers*

**Step 1: Set up an AWS Account and GitHub Repository**
1. Create an AWS account if you don't have one already.
2. Set up a GitHub repository where you'll store your code.

**Step 2: Configure AWS Credentials**
1. Generate an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. You can do this by going to the AWS Management Console, navigating to IAM (Identity and Access Management), and creating a new IAM user with appropriate permissions.
2. Store the AWS access key and secret access key securely. You'll need them later to configure GitHub Secrets.

**Step 3: Create a CloudFormation Template**
1. Write a CloudFormation template in YAML or JSON format that defines your AWS stack resources. In this example, we will be creating a  `stack.yml` with the necessary AWS resources defined within it.

**Step 4: Configure GitHub Secrets**

*# TODO: Add all varibles needed*
*# TODO: add picture*

1. In your GitHub repository, go to "Settings" and select "Secrets".
2. Create two secrets: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Set the values to the access key and secret access key you generated in Step 2.


**Step 5: Set up GitHub Actions**

*# TODO: add forking informaotin here*
*# TODO: add to reflect what this deploy is doing

1. In your GitHub repository, create a new directory named `.github/workflows`.
2. Inside the `.github/workflows` directory, create a new YAML file (e.g., `deploy.yml`) to define your workflow.
3. Add the following code to the `deploy.yml` file:

```yaml
name: Deploy AWS Stack
on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Deploy AWS CloudFormation stack
        run: aws cloudformation deploy --template-file stack.yml --stack-name MyStack --capabilities CAPABILITY_IAM
```

4. Make sure to replace `stack.yml` with the name of your CloudFormation template file, and `MyStack` with the desired stack name.

**Step 6: Push Code to Trigger Deployment**
1. Commit and push your CloudFormation template file (`stack.yml`) to the main branch of your GitHub repository.

That's it! Now, whenever you push changes to your CloudFormation template in the main branch of your GitHub repository, the GitHub Actions workflow will be triggered, deploying your AWS CloudFormation stack. You can view the deployment progress and any potential errors in the Actions tab of your GitHub repository.

Note: This example uses the AWS CLI to deploy the stack. Make sure the machine running the GitHub Actions workflow has the AWS CLI installed and configured with appropriate permissions to deploy the stack.


This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
