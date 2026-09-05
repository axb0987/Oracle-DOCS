# Moving a Private View Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm
- Fetched: 2026-09-05 01:58 CDT

# Moving a Private View Between Compartments

Move a private domain name service (DNS) view from one compartment to another.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

See[Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/privatedns.htm)and[Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm)for a feature overview and more information about private views.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm#)
- 

- On the Private views list page, find the private view you want to work with. If you need help finding the list page, see[Listing Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-list.htm#top).
- From the Actions menu (three dots) for the view, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[view change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/change-compartment.html)command and required parameters to move a view to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeViewCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/ChangeViewCompartment)
