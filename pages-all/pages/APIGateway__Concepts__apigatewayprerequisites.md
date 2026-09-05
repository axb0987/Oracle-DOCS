# Preparing for API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayprerequisites.htm
- Fetched: 2026-09-05 01:37 CDT

# Preparing for API Gateway

Find out about the high-level prerequisites for using API Gateway.

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

## Availability by Region

The API Gateway service is available in the Oracle Cloud Infrastructure regions listed at[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)
