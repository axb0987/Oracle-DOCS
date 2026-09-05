# Deleting a Private View
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting a Private View

Delete a private domain name service (DNS) view and its associated private zones.

See[Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm)and[Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/views.htm)for a feature overview and more information.
Note  
  
Protected private zones are managed by other OCI services, so you can't delete them directly. For example, if a protected zone was created because a subnet was created, then deleting the subnet would delete the zone.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

Caution  
  
Deletion removes any associated private zones.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm#)
- 

- On the Private views list page, find the private view you want to work with. If you need help finding the list page, see[Listing Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-list.htm#top).
- From the Actions menu (three dots) for the private view you want to delete, select Delete .
- In the Delete DNS private view dialog box, review the private view and the zones to be deleted.
- Enter`DELETE`to confirm the deletion.
- Select Delete all .
- 

Use the[view delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/delete.html)command and required parameters to delete a view and its associated zones:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteView](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/DeleteView)
