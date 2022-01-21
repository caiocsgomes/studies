# How to use CloudFormation parameters with an external file

If you are using a reusable CloudFormation template you'll probably want to use Parameters. Parameters are variables that you can use inside the template to input values each time you create or update a stack. This way the values are not hard-coded on the template and you can reuse it just changing the variables.

If you do not specify the parameters and upload the template using the console, CloudFormation will ask each of them when creating or updating the stack and you'll input on the console. Another approach is to have a parameters file for *prod* and *dev* and pass this file when creating the stack using the AWS CLI. This repository shows how to do that.

*parameters-dev.json* and *parameters-prod.json* are the parameters files. They have the same keys with different values.

*parameters-dev.json* file:
```json
[
    {
        "ParameterKey": "BucketVersioningConfiguration",
        "ParameterValue": "Suspended"
    },
    {
        "ParameterKey": "BucketAccessControl",
        "ParameterValue": "PublicRead"
    }
]
```

Then on the *template.yml* we just reference and use them:

```yml
Parameters:
  BucketAccessControl:
    Description: Bucket access control type
    Type: String
  BucketVersioningConfiguration:
    Description: Bucket versioning
    Type: String
  

Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      AccessControl: !Ref BucketAccessControl
      VersioningConfiguration:
        Status: !Ref BucketVersioningConfiguration
      Tags:
        - Key: type
          Value: example
```

To upload dev using the AWS CLI:

```sh
aws cloudformation create-stack --stack-name parameters-separate-files-dev --template-body file://template.yml --parameters file://parameters-dev.json
```

To upload prod using the AWS CLI:
```sh
aws cloudformation create-stack --stack-name parameters-separate-files-prod --template-body file://template.yml --parameters file://parameters-prod.json
```