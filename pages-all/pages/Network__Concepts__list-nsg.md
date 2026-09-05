# Listing NSGs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm
- Fetched: 2026-09-05 02:41 CDT

# Listing NSGs

List the network security groups (NSGs) in a Virtual Cloud Network (VCN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the NSG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Network Security Groups section.
- Under Resources , select Network Security Groups .

All NSGs in the VCN are displayed in a table.
- 

Use the[network nsg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/list.html)command and required parameters to list the NSGs in a VCN:

```

```

You must specify either a`--vlan-id`or a`--compartment-id`, but can't specify both. If you specify a`--vlan-id`, all other parameters are ignored.

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListNetworkSecurityGroups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/ListNetworkSecurityGroups)
