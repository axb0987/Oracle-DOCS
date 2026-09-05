# Moving a DNS Zone Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm
- Fetched: 2026-09-05 01:59 CDT

# Moving a DNS Zone Between Compartments

Move a domain name service (DNS) zone from one compartment to another.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

For more information about DNS, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm#)
- 

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Under List scope , select the compartment that contains the zone.
- Find the zone in the list, select its Actions menu (three dots), and select Move resource .
- Select a destination compartment from the list.
- Select Move resource .
- 

Use the[zone change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/change-compartment.html)command and required parameters to move a zone to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeZoneCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/ChangeZoneCompartment)
