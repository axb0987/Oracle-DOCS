# Blocking or Allowing Traffic for a NAT Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm
- Fetched: 2026-09-05 02:45 CDT

# Blocking or Allowing Traffic for a NAT Gateway

Block or allow traffic for a NAT gateway.

You create a NAT gateway in the context of a specific VCN. The NAT gateway is automatically always attached to only one VCN. However, you can block or allow traffic through the NAT gateway at any time. By default, the gateway allows traffic upon creation. Blocking the NAT gateway prevents all traffic from flowing, regardless of any existing route rules or security rules in the VCN.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the NAT Gateways section.
- Under Resources , select NAT Gateways .
- For the NAT gateway you're interested in, select the Actions menu (three dots) , and then select Block Traffic (or Allow Traffic if you previously blocked traffic).
- Select Block Traffic (or Allow Traffic if you previously blocked traffic) to confirm.

When the traffic is blocked, the NAT gateway's icon turns gray, and the label changes to BLOCKED. When the traffic is allowed, the NAT gateway's icon turns green, and the label changes to AVAILABLE.
- 

Use the[network nat-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/update.html)command and required parameters to block (true) or allow (false) traffic for a NAT gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/UpdateNatGateway)
