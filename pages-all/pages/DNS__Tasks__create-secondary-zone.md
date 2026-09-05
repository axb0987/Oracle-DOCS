# Creating a Secondary DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm
- Fetched: 2026-09-05 01:58 CDT

# Creating a Secondary DNS Zone

Create a secondary domain name service (DNS) zone to set up ingress from an external DNS provider to Oracle Cloud Infrastructure (OCI) DNS.

This topic describes how to set up an OCI secondary zone that accepts zone transfers from an external DNS provider (secondary ingress). To set up a scenario where a primary OCI DNS zone transfers to a secondary external DNS provider (secondary egress), see the[Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm)overview page.

Secondary ingress DNS requires that you define the zone name and the IP addresses of the primary external server during the secondary zone creation process. Also, you need connectivity to OCI IP addresses on the externally managed primary DNS servers. Connectivity to OCI IP addresses is a requirement for secondary DNS because it lets the service perform the required zone transfer process from the primary DNS to keep the secondary zone in sync.
You can obtain the OCI IP addresses that perform the zone transfers from the primary DNS in one of the following ways:
- Use the OCI API before you begin setup.[ListZoneTransferServers](https://docs.oracle.com/iaas/api/#/en/dns/latest/ZoneTransferServer/ListZoneTransferServers)returns a list of IP addresses provided for the specified root compartment. The provided transfer name server IP addresses vary by region. For more information, see[Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm).
- If you're using the Console, the list of zone transfer servers appears in the Create public zone page.

You can optionally configure a secondary DNS zone to use a TSIG key. If you don't already have an existing TSIG key, create one before you begin setting up the secondary DNS zone. For more information, see[Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm).

See[Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm)for a feature overview and more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm#)
- 

- On the Public zones list page, select Create Zone . If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- For Method , select Manual .
- For Zone type , select Secondary .
- Enter a descriptive name for the zone. Avoid entering confidential information.
- Specify the compartment to create the zone in. Be sure you have permission to work in the compartment.

Important  
  
Ensure the primary nameservers can accept a transfer request from the list of OCI zone transfer destination IP addresses provided in the Create public zone panel.
- For Upstream server IP , add an external upstream nameserver IP address. Select Add additional server IP to add more upstream server IP addresses.
- (Optional) Select a[TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm).
- Select Create .
- 

Use the[zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html)command and required parameters to create a secondary zone:

```

```

The`external-masters`option becomes a required parameter when the zoneType value is SECONDARY .

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)operation to create a secondary zone. Specify the`zoneType`as`SECONDARY`and the scope as`GLOBAL`.

The`externalMasters`
