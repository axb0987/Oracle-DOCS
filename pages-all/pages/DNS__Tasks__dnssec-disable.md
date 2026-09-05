# Disabling DNSSEC on a Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm
- Fetched: 2026-09-05 01:58 CDT

# Disabling DNSSEC on a Zone

Disable DNS security extensions (DNSSEC) on a public zone.

To avoid service disruptions, follow these steps in the order presented to disable DNSSEC.

- Remove DS records for the zone from all child zone delegation subdomains. See[Changing DNS Zone Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm)for information about updating OCI zone records.
- Remove the DS record from the parent zone.
- Wait until the TTL (time to live) for the removed parent zone DS record expires.
- Either[delete the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm)or disable DNSSEC on the zone.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm#)
- 

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- In Zone information , under DNSSEC, select Edit .
- Select the DNSSEC switch to Disabled .
- Select Save changes .
- 

Use the[zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html)command and required parameters to update the zone. To disable DNSSEC, specify the`dnssec-state`as`DISABLED`.:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone)operation to update the zone. To disable DNSSEC, specify the`dnssecState`as`DISABLED`
