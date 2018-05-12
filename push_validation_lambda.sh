#!/bin/bash

# NOTE to change the S3 bucket name
pushd pipeline/codepipeline-lambda
zip -r codepipeline-lambda.zip *
aws s3 cp 'codepipeline-lambda.zip'  s3://sf-aws-security-week-2018/pipeline/
rm 'codepipeline-lambda.zip'
popd
