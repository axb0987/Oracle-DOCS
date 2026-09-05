# Updating a Secondary DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm
- Fetched: 2026-09-05 01:59 CDT

# Updating a Secondary DNS Zone

Update the master server IP information for a secondary domain name service (DNS) zone.

Tip  
  
For OCI to transfer data from a zone, the nameservers must accept a transfer request from the following IP addresses: 208.78.68.65, 204.13.249.65, 2600:2001:0:1::65, 2600:2003:0:1::65

Information such as zone name and type aren't editable after you create a zone.

To update zone records for a primary zone, see[Changing DNS Zone Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm).

For general information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm#)
- 

- On the Public zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Select Upstream servers .
- Select Manage upstream servers .
- Make the changes to the existing upstream server information.
- (Optional) Select Add additional server IP to add another server IP address.
- Select Submit .

Tip  
  
For OCI to transfer data from the zone, the nameservers must accept a transfer request from the following IP addresses: 208.78.68.65, 204.13.249.65, 2600:2001:0:1::65, 2600:2003:0:1::65
- 

Use the[zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html)command and required parameters to update the master server IP addresses of a secondary zone:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone)
