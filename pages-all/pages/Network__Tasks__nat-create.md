# Creating a NAT Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm
- Fetched: 2026-09-05 02:45 CDT

# Creating a NAT Gateway

Create a NAT gateway in a virtual cloud network (VCN) in Networking.

Prerequisites:
- Decide which private subnets in the VCN need access to the internet, and create those private subnets.

Only one NAT gateway is needed for each VCN. All private subnets within a VCN have access to the NAT gateway if the security rules and route table rules allow that access.
- You can configure the types of ingress and egress internet traffic route rules that you want to enable for the resources in each public subnet (examples: ingress HTTPS connections, ingress ICMP ping connections).
- The required IAM policy is in place to allow you to work with Networking service resources. For administrators, see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to create a NAT gateway in. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the NAT Gateways section and select Create NAT Gateway .
- Under Resources , select NAT Gateways , and then select Create NAT Gateway .
- Enter a friendly name for the gateway. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the gateway in. Select another compartment if needed.
- Specify whether the public IP address is reserved or ephemeral. Oracle generates an IP address for the gateway automatically.

- Ephemeral IP Address: Select this option to let Oracle specify an[ephemeral IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph)for you from the Oracle IP pool. This option is the default.
- Reserved IP Address: Select this option to specify an existing[reserved IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph)by name, or to create a new reserved IP address by assigning a name and selecting a source[IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ip_pools.htm)for the address. If you don't select a pool, the default Oracle IP pool is used.
- (Optional) In the Route Table Association section, you can associate a specific route table with this gateway. After you associate a route table, the gateway must always have a route table associated with it. You can change the rules in the current route table or replace it with another route table.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create NAT Gateway .

The NAT gateway is created and displayed on the NAT Gateways list. The gateway allows traffic by default. At any time, you can[block or allow traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm)through it.
- 

Use the[network nat-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/create.html)command and required parameters to create a NAT gateway in a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/CreateNatGateway)
