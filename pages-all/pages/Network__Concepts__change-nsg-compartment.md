# Moving an NSG to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm
- Fetched: 2026-09-05 02:41 CDT

# Moving an NSG to a Different Compartment

Move a network security group (NSG) in a Virtual Cloud Network (VCN) between compartments.

When you move an NSG to a new compartment, inherent policies apply immediately.

For more information about using compartments and policies to control access to resources in a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-nsg-compartment.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the NSG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Network Security Groups section.
- Under Resources , select Network Security Groups .
- From the Actions menu (three dots) for the NSG, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network nsg change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/change-compartment.html)command and required parameters to move an NSG from one compartment to another:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeNetworkSecurityGroupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/ChangeNetworkSecurityGroupCompartment)
