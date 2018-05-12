
## Automating Security and Compliance Testing of Infrastructure-as-Code for DevSecOps

```
AWS Security Week SF
May 2018

Lab by:
Alex Corstorphine - senior cloud solutions architect, Dome9 Security
Roy Feintuch - co-founder & CTO, Dome9 Security

www.dome9.com
```

### Setup Instructions
1. Clone this repo or download from github
1. Create your own S3 bucket in the desired region and **enable versioning** on the bucket 
1. Review the push___.sh scripts and **UPDATE** your S3 bucket name
1. Upload (to S3) the pipline validation code: `./push_validation_lambda.sh`
1. Create new stack in the CloudFormation service using `pipeline-cft.json` . Fill our the parameters, and click next.next...
1. View your brand new pieline on AWS CodePipline page (it should fail as we didn't push our app yet)
1. Test your pipeline by uploading your first 'app' `./push_app.sh exercises/level1`

### Test Instructions
Once you have a working pipeline, start following the exercises in the `exercises` folder
For each level test a non-valid sample (which should fail) and a valid one which should pass.
```bash
./push_app.sh exercises/level1/valid
```
