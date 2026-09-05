# Connecting to Oracle Autonomous AI Database Instances from Running Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingadbfromrunningfunctions.htm
- Fetched: 2026-09-05 02:07 CDT

# Connecting to Oracle Autonomous AI Database Instances from Running Functions

Find out how to connect to Oracle Autonomous AI Database instances from running functions deployed to OCI Functions.

You can deploy a function to OCI Functions that connects to Oracle Autonomous AI Database instances.

Note that an Oracle Autonomous AI Database instance can be protected by an access control list (ACL). If the ACL is enabled, only those IP addresses and VCNs explicitly added to the ACL are allowed to connect to the database.

If you want a function running in a private subnet to connect to an Oracle Autonomous Database instance that has ACL enabled, edit the database's access control list and add the VCN.

If you want a function running in a public subnet to connect to an Oracle Autonomous Database instance that has ACL enabled:
- Remove the default route rule that routes all outgoing internet traffic through the VCN's internet gateway.
- Add a NAT gateway to the VCN.
- Configure the subnet's route table with a rule that sends all outgoing internet traffic to the NAT gateway, and configure the subnet's security lists to allow internet traffic.
- Review the NAT gateway's properties to obtain its public IP address.
- Edit the database's access control list and add the NAT gateway's public IP address.

For more information about Oracle Autonomous AI Databases and ACLs, see[Configuring Network Access with Access Control Rules (ACLs) and Private Endpoints](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-network-access.html#GUID-D2D468C3-CA2D-411E-92BC-E122F795A413)
