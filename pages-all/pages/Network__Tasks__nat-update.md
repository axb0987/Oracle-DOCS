# Updating a NAT Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm
- Fetched: 2026-09-05 02:45 CDT

# Updating a NAT Gateway

Update the display name for a NAT gateway in a Virtual Cloud Network (VCN) in Networking.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the NAT Gateways section.
- Under Resources , select NAT Gateways .
- For the NAT gateway that you're interested in, select the Actions menu (three dots) , and then select Edit .
- Enter the new name and select Save Changes .
- 

Use the[network nat-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/update.html)command and required parameters to update the display name for a NAT gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/UpdateNatGateway)
