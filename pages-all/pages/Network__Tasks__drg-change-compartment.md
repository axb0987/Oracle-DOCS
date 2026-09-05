# Moving a DRG to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm
- Fetched: 2026-09-05 02:43 CDT

# Moving a DRG to a Different Compartment

Move a Dynamic Routing Gateway (DRG) from one compartment to another.

You can move a DRG from one compartment to another. When you move a DRG to a new compartment, policies applied to that compartment apply immediately to the DRG.

For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm#)
- 

- On the Dynamic Routing Gateways list page, find the DRG that you want to move. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- From the Actions menu (three dots) for the DRG, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network drg change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/change-compartment.html)command and required parameters to move a DRG from one compartment to another:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeDrgCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/ChangeDrgCompartment)
