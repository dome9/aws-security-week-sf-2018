#!/bin/bash

# a 'deployment' script based on S3
# In real world we would probably have a pipline configured to our git repository
S3_BUCKET=sf-aws-security-week-2018

if [ "$1" != "" ]; then
    echo "Uploading app CFT from folder $1"
else
    echo "Please provide a folder with a CFT file"
    exit 1
fi

test_folder=$1
pushd $test_folder
rm -f my-app-cft.zip
zip -r my-app-cft.zip myapp.json
aws s3 cp 'my-app-cft.zip'  s3://$S3_BUCKET/artifacts/
rm -f my-app-cft.zip
popd