# Moving a CPE to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm
- Fetched: 2026-09-05 02:43 CDT

# Moving a CPE to a Different Compartment

Move a CPE from one compartment to another.

You can move a CPE object from one compartment to another. When you move a CPE to a new compartment, policies applied to that compartment apply immediately to the CPE.

For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm#)
- 

- On the Customer-premises equipment list page, find the CPE that you want to move. If you need help finding the list page, see[Listing CPEs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm).
- From the Actions menu (three dots) for the CPE, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network cpe change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/change-compartment.html)command and required parameters to move a CPE from one compartment to another:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeCpeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/ChangeCpeCompartment)
