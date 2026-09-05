# Moving a Security List to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm
- Fetched: 2026-09-05 02:41 CDT

# Moving a Security List to a Different Compartment

Move a security list in a Virtual Cloud Network (VCN) to a different compartment.

You can move security lists from one compartment to another. Moving a security list doesn't affect its attachment to a subnet. When you move a security list to a new compartment, inherent policies apply immediately and affect access to the security list. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the security list you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Security Lists section.
- Under Resources , select Security Lists .
- From the Actions menu (three dots) for the security list, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network security-list change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/change-compartment.html)command and required parameters to move a security list to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeSecurityListCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/ChangeSecurityListCompartment)
