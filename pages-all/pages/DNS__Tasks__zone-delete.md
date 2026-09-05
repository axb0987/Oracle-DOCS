# Deleting a DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting a DNS Zone

Delete a domain name service (DNS) zone and its records.

Caution  
  
Deletion permanently removes a zone and its records from the DNS service.
Note  
  
Protected private zones are managed by other OCI services, so you can't delete them directly. For example, if a protected zone was created because a subnet was created, then deleting the subnet would delete the zone.

For more information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#)
- 

- On the Public zones or Private zones list page, find the zone you want to delete. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- From the Actions menu (three dots) for the zone you want to delete, select Delete .
- Enter the zone name to confirm the deletion, and then select Delete .
- 

Use the[zone delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/delete.html)command and required parameters to delete a zone:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/DeleteZone)
