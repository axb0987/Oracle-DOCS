# Creating an Internet Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating an Internet Gateway

Create an internet gateway (IGW) in a Virtual Cloud Network (VCN) in Networking.

Prerequisites:
- Decide which public subnets in the VCN need access to the internet, and create those public subnets.

Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway if the security rules and route table rules allow that access.
- You can configure the types of ingress and egress internet traffic route rules that you want to enable for the resources in each public subnet (examples: ingress HTTPS connections, ingress ICMP ping connections).
- The required IAM policy is in place to allow you to work with Networking service resources. For administrators, see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).
Important  
  

If the public subnet is configured to use the[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default), remember that the list includes several helpful default rules that enable basic required access (examples: ingress SSH, egress access to all destinations). We recommend that you become familiar with the basic access that these default rules provide. If you decide not to use the default security list, be sure to provide this basic access by implementing these security rules either in[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)(NSGs) or custom[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm). You also need to[configure route rules in the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)used by the public subnets to allow traffic to be routed to and from the internet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Internet Gateways section and select Create Internet Gateway .
- Under Resources , select Internet Gateway and select Create Internet Gateway .
- Enter a friendly name for the gateway. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the gateway in. Select another compartment if needed.
- (Optional) In the Route Table Association section, you can associate a specific route table with this gateway. After you associate a route table, the gateway must always have a route table associated with it. You can change the rules in the current route table or replace it with another route table.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create Internet Gateway .

The internet gateway is created and displayed on the Internet Gateways list. You still need to[add a route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)that allows traffic to flow to the internet gateway, and explicitly[allow that traffic with a security rule in a security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/update-securitylist.htm)or[network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/manage-nsg-security-rules.htm).
- 

Use the[network internet-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/create.html)command and required parameters to create a new internet gateway for the specified VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/CreateInternetGateway)operation to create a new internet gateway.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
