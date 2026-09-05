# Moving a Reserved Public IP to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm
- Fetched: 2026-09-05 02:47 CDT

# Moving a Reserved Public IP to a Different Compartment

Move a reserved public IP address from one compartment to another. When you move a reserved public IP to a new compartment, inherent policies apply immediately.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select Reserved public IPs .
- For the reserved public IP you want to edit, select the Actions menu (three dots) , and then select Move resource .
- Select a destination compartment from the list, and then select Move resource .
For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
- 

Use the[network public-ip change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/change-compartment.html)command and required parameters to move a public IP to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangePublicIpCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/ChangePublicIpCompartment)
