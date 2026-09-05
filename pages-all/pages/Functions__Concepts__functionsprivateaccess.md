# OCI Functions Support for Private Network Access
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsprivateaccess.htm
- Fetched: 2026-09-05 02:07 CDT

# OCI Functions Support for Private Network Access

Find out about how OCI Functions supports private network access to enable private communication between functions and other resources.

OCI Functions supports private communication between a function in a VCN and other Oracle Cloud Infrastructure resources and[supported services in the Oracle Services Network](https://www.oracle.com/cloud/networking/service-gateway.html)without the traffic going over the internet. You can:
- enable a function in the VCN to access other resources and services
- enable other resources and services to invoke functions in the VCN

To provide such private access:
- create and deploy functions in private subnets
- add a service gateway to the VCN

For more information, see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)
