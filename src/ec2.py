RDS_SECURITY_GROUP= "my-rds-public-sg-mv"
class EC2:
    def __init__(self, client):
        self._client == client
        """ :type : pyboto3.ec2 """


    def create_security_group(self):
        print("creating a aws security group")
        self._client.create_security_group(
            GroupName=RDS_SECURITY_GROUP,
            Description="Tutorial learning boto",
            vpc="TODO")
    
    def add_inbound_rule_to_sg(self):
        print("add inbound access rule to security group")
        self._client.authorize_security_group_ingress(
            GroupId= security_group_id,
            IdPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 5432,
                    'ToPort': 5432,
                    'IpRanges': [{'CidrIp':'0.0.0.0/0'}]
                }
            ]
            
        )

