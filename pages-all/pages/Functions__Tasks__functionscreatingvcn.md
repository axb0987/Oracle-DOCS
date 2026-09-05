# Creating the VCN and Subnets to Use with OCI Functions, if they don't exist already
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingvcn.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating the VCN and Subnets to Use with OCI Functions, if they don't exist already

Find out how to create the VCN and subnets to use with OCI Functions, if they don't exist already.

Before users can start using OCI Functions to create and deploy functions, a VCN containing the subnets in which to create functions and applications must already exist. The VCN can be, but need not be, owned by the same compartment to which other function-related resources will belong.

The VCN must have a CIDR block that provides at least a certain minimum number of free IP addresses for OCI Functions to use. For more information, see[CIDR Blocks and OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscidrblocks.htm).

To support the largest possible number of concurrent connections, Oracle strongly recommends that the security lists used by subnets in the VCN only have stateless rules.

If a suitable VCN already exists, there's no need to create a new one.

If you do decide to create a new VCN, you have several options, including the following:
- 

You can create the new VCN and have related resources created automatically at the same time, using one of the VCN wizards (such as the VCN with Internet Connectivity wizard). As well as creating the VCN, the VCN with Internet Connectivity wizard creates a public regional subnet and a private regional subnet, along with an internet gateway, a NAT gateway, and a service gateway. The VCN with Internet Connectivity wizard also creates route tables and security lists. For more information about the VCN wizards, see[Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
- 

You can create just the VCN initially, and then create the related resources yourself later (see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)). In this case, you can choose which of the following to create:
- 

Public subnets and an internet gateway (see[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)). In this case, a route table must include a route rule that targets the internet gateway, with its Destination CIDR Block property set to 0.0.0.0/0. A security list must include a stateful egress rule that allows access to Oracle Cloud Infrastructure Registry (for example, with its Destination Type property set to`Service`, its Destination Service property set to`All <region> services In Oracle Services Network`, and its IP Protocol property set to`All`).
- 

Private subnets and a service gateway (see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)). In this case, the service gateway must be set up to allow access to`All <region> Services In Oracle Services Network`. A route table must include a route rule that targets the service gateway, with its Destination Service property set to`All <region> Services In Oracle Services Network`. A security list must include a stateful egress rule that allows access to Oracle Cloud Infrastructure Registry (for example, with its Destination Type property set to`Service`, its Destination Service property set to`All <region> services In Oracle Services Network`, and its IP Protocol property set to`All`).

For example, if you don't want to expose traffic over the public internet, create private subnets and a service gateway (see[OCI Functions Support for Private Network Access](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsprivateaccess.htm)).

Note that to use an external logging destination like Papertrail, you have to create a VCN with public subnets (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)
