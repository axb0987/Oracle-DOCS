# Example Network Resource Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewaynetworkconfigexample.htm
- Fetched: 2026-09-05 01:37 CDT

# Example Network Resource Configurations

Find out about examples of how you might configure network resources for API gateway development.

Before you can use the API Gateway service to create API gateways and deploy APIs on them as API deployments:
- You must have access to an Oracle Cloud Infrastructure tenancy. The tenancy must be subscribed to one or more of the regions in which API Gateway is available (see[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/../Concepts/apigatewayprerequisites.htm#regional-availability)).
- 

Your tenancy must have sufficient quota on API Gateway-related resources (see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)).
- Within your tenancy, there must already be a compartment to own the necessary network resources. If such a compartment does not exist already, you will have to create it. See[Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/../Tasks/apigatewaycreatingcompartment.htm).
- The compartment that owns network resources must contain a VCN, a public or private regional subnet, and other resources (such as an internet gateway, a route table, security lists and/or network security groups). To ensure high availability, API gateways can only be created in regional subnets (not AD-specific subnets). Note that an API gateway must be able to reach the back ends defined in the API deployment specification. For example, if the back end is on the public internet, the VCN must have an internet gateway to enable the API gateway to route requests to the back end.
- 

The VCN must have a set of DHCP options that includes an appropriate DNS resolver to map host names defined in an API deployment specification to IP addresses. If such a DHCP options set does not exist in the VCN already, you will have to create it. Select the DHCP options set for the API gateway's subnet as follows:
- If the host name is publicly published on the internet, or if the host name belongs to an instance in the same VCN, select a DHCP options set that has the Oracle-provided Internet and VCN Resolver as the DNS Type . This is the default if you do not explicitly select a DHCP options set.
- If the host name is on your own private or internal network (for example, connected to the VCN by FastConnect), select a DHCP options set that has Custom Resolver as the DNS Type , and has the URL of a suitable DNS server that can resolve the host name to an IP address.

Note that you can change the DNS server details in the DHCP options set specified for an API gateway's subnet. The API gateway will be reconfigured to use the updated DNS server details within two hours. For more information about resolving host names to IP addresses, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).
- Within your tenancy, there must already be a compartment to own API Gateway-related resources (API gateways, API deployments). This compartment can be, but need not be, the same compartment that contains the network resources. See[Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/../Tasks/apigatewaycreatingcompartment.htm). Note that the API Gateway-related resources can reside in the root compartment. However, if you expect multiple teams to create API gateways, best practice is to create a separate compartment for each team.
- 

To create API gateways and deploy APIs on them, you must belong to one of the following:
- The tenancy's Administrators group.
- 

A group to which policies grant the appropriate permissions on network and API Gateway-related resources. See[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/../Tasks/apigatewaycreatingpolicies.htm).
- Policies must be defined to give the API gateways you create access to additional resources, if necessary. See[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/../Tasks/apigatewaycreatingpolicies.htm).

This topic gives examples of how you might configure network resources for API gateways with a serverless function as a back end:
- for a public API gateway in a public subnet (see[Example 1: Example Network Resource Configuration for a Public API Gateway in a Public Subnet with a Serverless Function as an HTTP Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewaynetworkconfigexample.htm#example-public-api-gateway))
- for a private API gateway in a private subnet (see[Example 2: Network Resource Configuration for a Private API Gateway in a Private Subnet with a Serverless Function as an HTTP Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewaynetworkconfigexample.htm#example-private-api-gateway))

These examples assume the default helloworld function has been created and deployed in OCI Functions with the name helloworld-func and belonging to the helloworld-app application (see[Creating, Deploying, and Invoking a Helloworld Function](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingfirst.htm)).
Note  
  

The examples in this section show the use of security rules in security lists to control access. If you prefer network security groups over security lists, you can specify identical security rules for network security groups.

## Example 1: Example Network Resource Configuration for a Public API Gateway in a Public Subnet with a Serverless Function as an HTTP Back End

This example assumes you want a public API gateway that can be accessed directly from the internet, with a serverless function as an HTTP back end.

[

To achieve this example configuration, you create the following resources in the sequence shown, with the properties shown in the Example Resource Configuration table below:
- A VCN named 'acme-vcn1'.
- An internet gateway named 'acme-internet-gateway'.
- A route table named 'acme-routetable-public'.
- A security list named 'acme-security-list-public', with an ingress rule that allows public access to the API gateway and an egress rule that allows access to OCI Functions.
- A public subnet named 'acme-public-subnet'.
- An API gateway named 'acme-public-gateway', with an API deployment named 'acme-public-deployment'.

Issuing a curl command from the public internet against the API deployment returns the response shown:
```

```

### Example Network Resource Configuration

Resource Example
VCN

Created manually, and defined as follows:
- Name: acme-vcn1
- CIDR Block: 10.0.0.0/16
- DNS Resolution: Selected
Internet Gateway

Created manually, and defined as follows:
- Name: acme-internet-gateway
Route Table

One route table created manually, named, and defined as follows:
- 

Name: acme-routetable-public, with a route rule defined as follows:
- Destination CIDR block: 0.0.0.0/0
- Target Type: Internet Gateway
- Target Internet Gateway: acme-internet-gateway
DHCP Options

Created automatically and defined as follows:
- DNS Type set to Internet and VCN Resolver
Security List

One security list created manually (in addition to the default security list), named, and defined as follows:
- Security List Name: acme-security-list-public, with an ingress rule that allows public access to the API gateway, and an egress rule that allows access to OCI Functions.
- Ingress Rule 1:
- State: Stateful
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 443
- Egress Rule 1:
- State: Stateful
- Destination Type: CIDR
- Destination CIDR: 0.0.0.0/0
- IP Protocol: All Protocols
Subnet

One regional public subnet created manually, named, and defined as follows:
- 

Name: acme-public-subnet with the following properties:
- CIDR Block: 10.0.0.0/24
- Route Table: acme-routetable-public
- Subnet access: Public
- DNS Resolution: Selected
- DHCP Options: Default
- Security List: acme-security-list-public
API Gateway

One public API gateway created and defined as follows:
- Name: acme-public-gateway
- Type: Public
- VCN: acme-vcn1
- Subnet: acme-public-subnet
- Hostname: (for the purpose of this example, the hostname is lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com)
API Deployment

One API deployment created and defined as follows:
- Name: acme-public-deployment
- Path Prefix: /marketing
- API Request Policies: None specified
- API Logging: None specified
- Route:
- Path: /hello
- Methods: GET
- Type: OCI Functions
- Application: helloworld-app
- Function Name: helloworld-func

## Example 2: Network Resource Configuration for a Private API Gateway in a Private Subnet with a Serverless Function as an HTTP Back End

This example assumes you want a private API gateway that can only be accessed via a bastion host (rather than accessed directly from the internet), with a serverless function as an HTTP back end.

[

To achieve this example configuration, you create the following resources in the sequence shown, with the properties shown in the Example Resource Configuration table below:
- A VCN named acme-vcn2
- An internet gateway named acme-internet-gateway
- A service gateway named acme-service-gateway. (In this example, you only need to create a service gateway, because the API gateway only has an OCI Functions back end. However, if the API gateway has both an OCI Functions back end and also an HTTP back end on the public internet, you could create a NAT gateway instead to access both back ends.)
- A route table named acme-routetable-private
- A security list named acme-security-list-private, with an ingress rule that allows the bastion host to access the API gateway and an egress rule that allows access to OCI Functions.
- A private subnet named acme-private-subnet
- An API gateway named acme-private-gateway, with an API deployment named acme-private-deployment
- A route table named acme-routetable-bastion
- A security list named acme-security-list-bastion, with an ingress rule that allows public SSH access to the bastion host and an egress rule that allows the bastion host to access the API gateway.
- A public subnet named acme-bastion-public-subnet
- A compute instance with a public IP address to act as the bastion host, called acme-bastion-instance

Having SSH'd into the bastion host, issuing a curl command against the API deployment returns the response shown:
```

```

### Example Resource Configuration

Resource Example
VCN

Created manually, and defined as follows:
- Name: acme-vcn2
- CIDR Block: 10.0.0.0/16
- DNS Resolution: Selected
Internet Gateway

Created manually, and defined as follows:
- Name: acme-internet-gateway
Service Gateway

Created manually, and defined as follows:
- Name: acme-service-gateway
- Services: All &lt;region&gt; Services in Oracle Services Network
Route Tables

Two route tables created manually, named, and defined as follows:
- 

Name: acme-routetable-bastion, with a route rule defined as follows:
- Destination CIDR block: 0.0.0.0/0
- Target Type: Internet Gateway
- Target Internet Gateway: acme-internet-gateway
- 

Name: acme-routetable-private, with a route rule defined as follows:
- Destination CIDR block: 0.0.0.0/0
- Target Type: Service Gateway
- Destination Service: All &lt;region&gt; Services in Oracle Services Network
- Target Service Gateway: acme-service-gateway
DHCP Options

Created automatically and defined as follows:
- DNS Type set to Internet and VCN Resolver
Security List

Two security lists created manually (in addition to the default security list), named, and defined as follows:
- 

Security List Name: acme-security-list-bastion,with an ingress rule that allows public SSH access to the bastion host and an egress rule that allows the bastion host to access the API gateway:
- Ingress Rule 1:
- State: Stateful
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 22
- Egress Rule 1:
- State: Stateful
- Destination Type: CIDR
- Destination CIDR: 0.0.0.0/0
- IP Protocol: All Protocols
- 

Security List Name: acme-security-list-private, with an ingress rule that allows the bastion host to access the API gateway and an egress rule that allows access to OCI Functions:
- Ingress Rule 1:
- State: Stateful
- Source Type: CIDR
- Source CIDR: 10.0.0.0/16
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 443
- Egress Rule 1:
- State: Stateful
- Destination Type: CIDR
- Destination CIDR: 0.0.0.0/0
- IP Protocol: All Protocols
Subnet

Two regional subnets created manually, named, and defined as follows:
- 

Name: acme-bastion-public-subnet, with the following properties:
- CIDR Block: 10.0.1.0/24
- Route Table: acme-routetable-bastion
- Subnet access: Public
- DNS Resolution: Selected
- DHCP Options: Default
- Security List: acme-security-list-bastion
- 

Name: acme-private-subnet, with the following properties:
- CIDR Block: 10.0.2.0/24
- Route Table: acme-routetable-private
- Subnet access: Private
- DNS Resolution: Selected
- DHCP Options: Default
- Security List: acme-security-list-private
API Gateway

One private API gateway created and defined as follows:
- Name: acme-private-gateway
- Type: Private
- VCN: acme-vcn2
- Subnet: acme-private-subnet
- Hostname: (for the purpose of this example, the hostname is pwa...djt.apigateway.us-phoenix-1.oci.customer-oci.com)
API Deployment

One API deployment created and defined as follows:
- Name: acme-private-deployment
- Path Prefix: /marketing-private
- API Request Policies: None specified
- API Logging: None specified
- Route:
- Path: /hello
- Methods: GET
- Type: OCI Functions
- Application: helloworld-app
- Function Name: helloworld-func
Instance

One compute instance created and defined as follows:
- Name: acme-bastion-instance
- Availability Domain: AD1
- Instance Type: Virtual Machine
- VCN: acme-vcn2
- Subnet: acme-bastion-public-subnet
-
