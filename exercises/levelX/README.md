
## Level X

In this level you'll be protecting against more exposed administrative ports.<br/>

Administrative ports such as SSH and RDP should never be open to the entire internet, but only exposed (if at all) to a small number of IP addresses.

### Your challenge
Do not allow security groups to open SSH port (TCP 22) to the entire internet (CIDR: 0.0.0.0/0)

You should allow to open this port to specific IP addresses.


### Tips
- Review the valid / nonvalid samples for insights regarding structure
- Review AWS documentation for Security Group CFT resource : https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html
- Don't trust the regex. There's more to look for



Good luck