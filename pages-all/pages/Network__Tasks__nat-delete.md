# Deleting a NAT Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm
- Fetched: 2026-09-05 02:45 CDT

# Deleting a NAT Gateway

Delete a NAT gateway from a Virtual Cloud Network (VCN) in Networking.

Prerequisite: Before you delete a NAT gateway, delete all route rules in the VCN that specify the gateway as the target. Deleting those rules stops the routing in the VCN to the gateway. If a route rule refers to the gateway, it can't be deleted until the reference is removed.

See[Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)and[Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)for more about finding and updating route rules that reference a gateway.

This operation is asynchronous. The NAT gateway's lifecycleState state changes to TERMINATING temporarily until the NAT gateway is removed.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the NAT Gateways section.
- Under Resources , select NAT Gateways .
- From the Actions menu (three dots) for the gateway that you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network nat-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/delete.html)command and required parameters to delete a NAT gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/DeleteNatGateway)
