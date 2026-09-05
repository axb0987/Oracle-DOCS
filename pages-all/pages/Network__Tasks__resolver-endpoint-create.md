# Creating a Resolver Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm
- Fetched: 2026-09-05 02:47 CDT

# Creating a Resolver Endpoint

Create a resolver endpoint that can used for forwarding and listening to DNS queries to or from another private DNS system such as a peered VCN or an on-premises network.

[When you create a VCN and select the Use DNS hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#enable-dns-hostnames-vcn), this choice creates a[dedicated private DNS resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)and a default private view with system-managed zones.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)and[Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-resolver_endpoints.htm)for more information about resolvers and endpoints in the VCN.

See[Managing Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm)for more information about managing private zones and views.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-create.htm#)
- 

- From the Virtual Cloud Network Details screen for the VCN, look in the VCN Information tab and select the name of the DNS resolver for the VCN.
The private resolver's details page opens.
- Select Resolver endpoints .
The Resolver endpoints page opens. All endpoints in the resolver are listed in tabular form.
- Select Create Endpoint .
The Create Endpoint panel opens.
- Enter the following information:

- Name : Select a name for the endpoint. The name can use any combination of letters and numbers, but the only supported special character is an underscore.
- Choose a subnet compartment : Select compartment that contains the subnet you want.
- Choose a subnet : Select a subnet from the list.
- Ingress/Egress : Select the endpoint type from the following options. When you make this choice, you provide an IP address, or let Oracle assign one for the endpoint. This IP address is used by the resolver to forward DNS queries, or to listen for DNS queries from other systems. The IP address must be in the same CIDR block used by the VCN or subnet associated with the resolver.
- Listening : This is an IP address in the subnet used to listen for queries. If you don't provide an IP address, the system creates one for you.
- Forwarding : This is an IP address in the subnet from which queries can be forwarded. If you don't provide an IP address, the system creates one for you.

## Security Attributes

Apply security attributes to control access for your resolver endpoint through the Zero Trust Packet Routing (ZPR) service. See[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)for more information. You can apply up to three security attributes for a resolver endpoint.

Select Use ZPR security attributes to display the security attribute settings. Enter the following information for each security attribute:
- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. For more information, see[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm).
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.

Select Add security attribute again to add another attribute, up to a maximum of three.

## Network Security Groups

You can add the resolver endpoint to a network security group (NSG). For more information, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). You can add an endpoint to a maximum of five NSGs.

Select Use network security groups to control traffic to add the resolver endpoint to a network security group (NSG).

Enter the following information:
- Compartment : Select the compartment that contains the NSG you want from the list.
- Network security group : Select the NSG you want from the list.

Select Add network security group to add the resolver endpoint to another NSG.

## Tags

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

## Create the Resource

Select Create resolver endpoint . The new endpoint appears in the resolver endpoint list.
- 

Use the[resolver-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/create.html)command and required parameters to create a resolver endpoint:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/CreateResolverEndpoint)
