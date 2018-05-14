
## Level X

In this level we'll be back to protecting Security Groups from exposed adminsitrative ports<br/>
however, we'll take the red pill and start to understand the complexity of CloudFormation templates and the task of validating them.



### Your challenge
Do not allow security groups to open SSH port (TCP 22) to the entire internet (CIDR: 0.0.0.0/0)

You should allow to open this port to specific IP addresses.


### Tips
- Review the valid / nonvalid samples for insights regarding structure
- Review AWS documentation for Security Group CFT resource : https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html
- Review some advanced CFT concepts such as intrinsic functions : https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html
- Don't trust the regex. There's more to look for
- Some tips and examples of this complexity can be found here: https://speakerdeck.com/froyke/re-invent-2017-automating-security-and-compliance-testing-of-iac-for-devsecops?slide=13
- This little project might assist : https://github.com/Dome9/cft-simulator



Good luck
