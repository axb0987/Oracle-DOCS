# Managing a Resolver Endpoint's Network Security Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-manage-nsg.htm
- Fetched: 2026-09-05 02:47 CDT

# Managing a Resolver Endpoint's Network Security Groups

Add or remove a network security group (NSG) associated with a resolver endpoint.
Network security groups (NSGs) act as a virtual firewall for DNS resolver endpoints. An NSG consists of a set of ingress and egress[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)that apply only to the associated DNS resolver endpoints.

We recommend that you change security list or NSG security rules to allow traffic bound for UDP Port 53 (and optionally TCP Port 53) on the DNS listener endpoints.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)and[Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-resolver_endpoints.htm)for more information about resolvers and endpoints in the VCN.

## Adding a Network Security Group

- On the Resolver endpoints list page, select the endpoint that you want to work with. If you need help finding the list page or the endpoint, see[Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm).
The endpoints detail's page opens.
- Select Security .
The Security page opens.
- Find the Network security groups section and select Manage network security groups .
The Manage network security groups panel opens.
- Select up to five security groups to associate with the endpoint.
- When finished, select Add Network Security Groups .

### Using the Console

## Removing a Network Security Group

- On the Resolver endpoints list page, select the endpoint that you want to work with. If you need help finding the list page or the endpoint, see[Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm).
The endpoints detail's page opens.
- From the Actions menu (three dots) for the NSG you want, select Delete .
-
