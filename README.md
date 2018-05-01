# Configure Linux Red Hat 7 LVM via Ansible

## Table of Contents
**[Short Description](#short-description)**

**[Full Description](#full-description)**

**[Creat Volume for VM via AWS](#creat-volume-for-vm-via-aws)**

## Short Description
Ansible LVM

## Full Description
LVM configuration using Ansible 2.4/2.5 in Red Hat Enterprise Linux (RHEL) 7.4/7.5.

## Creat Volume for VM via AWS
You can create an Amazon EBS volume that you can then attach to any EC2 instance within the same Availability Zone.
### Create Volume
1st, open [Amazon EC2 console](https://console.aws.amazon.com/ec2/).

2nd, from the navigation bar, select the region in which you would like to create your volume. In the navigation pane, choose `ELASTIC BLOCK STORE`, `Volumes`. See images below:

![aws-volumes.png](img/aws-volumes.png "AWS Volumes")
