# Create a VCN to Use with API Gateway, If One Doesn't Already Exist
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingvcn.htm
- Fetched: 2026-09-05 01:38 CDT

# Create a VCN to Use with API Gateway, If One Doesn't Already Exist

Find out how to create a VCN for use with API Gateway.

Before users can start using the API Gateway service to create API gateways and deploy APIs on them, as a tenancy administrator you have to create one or more VCNs containing a public or private regional subnet in which to create API gateways.

The VCN can be, but need not be, owned by the same compartment to which other API Gateway-related resources will belong. To ensure high availability, API gateways can only be created in regional subnets (not AD-specific subnets). Note that an API gateway must be able to reach the back ends defined in the API deployment specification. For example, if the back end is on the public internet, the VCN must have an internet gateway to enable the API gateway to route requests to the back end. The VCN must have a set of DHCP options that includes an appropriate DNS resolver to map host names defined in an API deployment specification to IP addresses.

The public or private regional subnet in which to create API gateways must have a CIDR block that provides a minimum of 32 free IP addresses. Note that Oracle strongly recommends the CIDR block provides more than the minimum.

To support the largest possible number of concurrent connections, Oracle also strongly recommends that the security lists used by the subnet only have stateless rules.

If a suitable VCN already exists, there's no need to create a new one.

If you do decide to create a new VCN, you have several options, including the following:
- You can create just the VCN initially, and then create the regional subnets and other related resources later (as described in this topic). In this case, you can choose whether to create a public regional subnet and an internet gateway (see[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)), or a private regional subnet and a service gateway (see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)). For example, if you don't want to expose traffic over the public internet, create a private regional subnet and a service gateway.
- You can create the new VCN and have related resources created automatically at the same time by selecting the Start VCN Wizard option. In this case, a public regional subnet and a private regional subnet are created, along with an internet gateway, a NAT gateway, and a service gateway. Although a default security list is also created, you have to add a new stateful ingress rule for the regional subnet (either in a security list or in a network security group) to allow traffic on port 443. That's because API Gateway communicates on port 443, and port 443 is not open by default (see the corresponding step in this topic).

See[Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewaynetworkconfigexample.htm)for details of typical network configurations.

To create a VCN to use with API Gateway:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- 

Choose the compartment that will own the network resources (on the left side of the page). For example,`acme-network`.

The VCN can be, but need not be, owned by the same compartment to which API Gateway-related resources will belong. The page updates to display only the resources in the compartment you select.
- Select Create VCN to create a new VCN.
- 

In the Create a Virtual Cloud Network dialog box, enter the following:
- Name: A meaningful name for the VCN, such as`acme-apigw-vcn`. The name doesn't have to be unique, but you cannot change it later using the Console(although you can change it using the API). Avoid entering confidential information.
- Other details for the VCN (see[Creating a VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/create_vcn.htm)).
- 

Select Create VCN to create the VCN.

The VCN is created and displayed on the virtual cloud network details page in the compartment you chose.
- Select the Subnets tab, and select Create Subnet .
- 

In the Create Subnet dialog box, enter the following:
- Name: A meaningful name for the subnet, such as`acme-apigw-subnet`. The name doesn't have to be unique, but you cannot change it later using the Console(although you can change it using the API). Avoid entering confidential information.
- Subnet Type: Select Regional (Recommended) . To ensure high availability, API gateways can only be created in regional subnets (not AD-specific subnets).
- CIDR Block: A CIDR block that provides a minimum of 32 free IP addresses.
- DHCP Options: (Optional) Select a set of DHCP options that includes an appropriate DNS resolver to map host names defined in an API deployment specification to IP addresses. If you do not explicitly specify a DHCP options set, the default DHCP options set uses the Oracle-provided Internet and VCN Resolver to return IP addresses for host names publicly published on the internet, and host names belonging to an instance in the same VCN.
- Other details for the subnet (see[Creating a Subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm)).
- 

Select Create Subnet to create the subnet.

The subnet is created and displayed on the Subnets tab in the compartment you chose.

API Gateway communicates on port 443, which is not open by default. You have to add a new stateful ingress rule for the regional subnet to allow traffic on port 443.
- 

Select the name of the regional subnet, then select the Security tab. Select the name of the default security list, then the Security rules tab, and then select Add Ingress Rules and enter the following:
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 443
-
