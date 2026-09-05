# Adding Downstream Servers to a Primary DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm
- Fetched: 2026-09-05 01:58 CDT

# Adding Downstream Servers to a Primary DNS Zone

Set up secondary egress from OCI DNS to an external DNS provider.

Obtain the following items before you begin:
- IP addresses of the external downstream servers.
- (Optional) TSIG keys to assign to each downstream server.
- Ensure that externally managed primary DNS servers can access OCI egress nameservers. The OCI nameservers perform the required zone transfers that keep the secondary zone in sync. To list OCI egress nameserver IP addresses for the root compartment, see[Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm). The provided transfer name server IP addresses vary by region.

See[Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm)for more information and a feature overview.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#)
- 

- On the Public zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Select the Downstream servers tab.
- Select Manage downstream servers .
- Enter a downstream server IP address. The IP address can be IPv4 or IPv6.
- (Optional) Select a[TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm).
- (Optional) Select Add additional server IP to add more downstream servers.
- Select Submit .
- 

Use the[zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html)command and required parameters to update the external secondary (downstream) servers for a zone:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone)
