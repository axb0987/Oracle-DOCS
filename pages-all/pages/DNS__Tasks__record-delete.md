# Deleting a DNS Zone Record
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting a DNS Zone Record

Delete the records in a domain name service (DNS) zone.

For more information, see[Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm).

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm#)
- 

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Select the Records tab.

A list of records appear. Records that have the same name, type, and TTL are displayed as a single RRset.
- Select Manage records .
- Use the Filters option to filter by state or type.
- From the Actions menu (three dots) for the record that you want to delete, select Delete .
Record changes don't take effect until they're published in the next steps.
- Select Publish Changes .
- On the Confirm page, review the changes, and then select Confirm publish changes .
- 

Use the[record rrset delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/delete.html)command and required parameters to delete a record.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteRrset](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/DeleteRRSet)
