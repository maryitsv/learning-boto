import boto3
from src.client_factory import EC2Client
from src.ec2 import EC2


RDS_BD_SUBNET_NAME="my-rds-subnet-group-mv"

class RDS:
    def ___init__(self, client):
        self._client = client
        """ :type : pyboto3.rds """

    def test(self):
        self._client.create_db_instance()

    def create_db_subnet_group():
        print("creating a aws db subnet group")
        self._client.create_db_subnet_group(
            DBSubnetGroupName=RDS_BD_SUBNET_NAME,
            DBSubnetGroupDescription="Learning boto",
            SubnetIDs=["TODO..."]
        )

    def create_postgrestsq_intance(self):
        print("creating a aws rds postgres")
        security_group_id = self.create_db_security_group_add_rules();

        self.create_db_subnet_group();

        self._client.create_db_instance(
            DBName="MyPostgressSQL",
            DBIntanceIdentifier="mypostgresdb",
            DBInstanceClass="db.t2.micro",
            Engine="postgres",
            EngineVersion="9.6.6",
            Port="5432",
            MasterUser="postgres",
            MasterUserPassword="learningBoto",
            AllocateStorage=20,
            MultiAZ=False,
            StorageType="gp2",
            VpcSecurityGroupIds=[security_group_id],
            PublicAccessible=True,
            DBSubnetGroupName=RDS_BD_SUBNET_NAME,
            Tags=[
                {
                    Key:"Name",
                    Value:"mvs"
                }
            ]
        )

    def create_db_security_group_add_rules(self):
        ec2_client = EC2Client.get_client();
        ec2 = EC2(ec2_client)

        security_group = ec2.create_security_group()

        security_group_id = security_group['GroupId']

        print("created securty group with id: " + security_group_id)

        ec2.add_inbound_rule_to_sg(security_group_id)

        print("inbound add public access rule to security group with id: " + security_group_id)

        return security_group_id
