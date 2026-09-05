# Creating a Public DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm
- Fetched: 2026-09-05 01:58 CDT

# Creating a Public DNS Zone

Create a public domain name service (DNS) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers.

You can create primary public zones with publicly available domain names reachable on the internet. For more information, see[Public DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted.htm). You can also create a[secondary zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/secondary-dns.htm), which pulls records for the zone from an external primary server.
- 

The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at[support.oracle.com](http://support.oracle.com/).
- 

Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see[Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
- Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#)
- 

- On the Public zones list page, select Create Zone . If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/zone-list.htm#top).
- On the Create zone panel, select the method to use to create the zone, Manual or Import .
- If you chose the manual method, enter the zone information:

- Zone type: Select Primary .
- Zone name: Enter the domain name for the zone. For example,`mydomain.com.`Avoid entering confidential information.
- Create in compartment: Specify the compartment to create the zone in. Be sure you have permission to work in the compartment.
- If you chose the import method, then drag, select, or paste a[valid zone file](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Reference/formattingzonefile.htm)into the panel.

The zone is imported as a primary zone.
- (Optional) Configure one or more secondary servers to receive zone transfers.
- Select Add additional server IP .
- Enter a valid IPv4 or IPv6 address.
- Select a[TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/tsig.htm#manage-tsig).
For more information, see[Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/secondary-dns.htm)and[Adding Downstream Servers to a Primary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/add-downstream-servers-primary-zone.htm).
- (Optional) To apply tags to the zone, select Show Advanced Options .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- (Optional) Select Show Advanced Options: to enable DNSSEC.

Note  
  
You can't enable DNSSEC if you plan to use downstream servers with the zone. DNSSEC requires updates to the DS records on the zone. See[DNSSEC](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnssec.htm)for more information.
- Select Create .

The zone is created and published with the necessary SOA and NS records, and its details page is displayed.
Next:
- [Delegate the public zone with a registrar](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Delegating_Your_Zone.htm)
Note  
  
The zone doesn't work on the internet until delegation is complete.
- [Add records to the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/record-add.htm)

If you have problems, see[Troubleshooting DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/troubleshooting.htm).
- 

Use the[zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html)command and required parameters to create a public primary zone:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to a zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/record-add.htm).
- 

Run the[CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)operation to create a public primary zone. Specify the zone type as`PRIMARY`and zone scope as`GLOBAL`.

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to a zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/record-add.htm)
