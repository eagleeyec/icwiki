# Ansible

## Running adhoc commands using dynamic inventory

	 ansible -i pathto/ec2.py us-east-1 -m shell -a "ls -a" 


