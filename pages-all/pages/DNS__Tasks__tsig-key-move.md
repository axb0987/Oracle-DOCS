# Moving a TSIG Key Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm
- Fetched: 2026-09-05 01:59 CDT

# Moving a TSIG Key Between Compartments

You can move a TSIG key from one compartment to another.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

See[Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm)for more information about TSIG keys and how they're used in zones.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm#)
- 

- On the TSIG keys list page, find the key you want to work with. If you need help finding the list page, see[Listing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm#top).
- From the Actions menu (three dots) for the TSIG key, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[tsig change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/change-compartment.html)command and required parameters to move a TSIG key to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeTsigKeyCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/ChangeTsigKeyCompartment)
