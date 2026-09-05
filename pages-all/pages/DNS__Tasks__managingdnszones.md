# Managing DNS Service Zones
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm
- Fetched: 2026-09-05 01:59 CDT

# Managing DNS Service Zones

The Oracle Cloud Infrastructure DNS service lets you manage zones using the Console, CLI, or API.

A zone is a part of the domain name service (DNS) namespace. A Start of Authority record (SOA) defines a zone. A zone contains all labels underneath itself in the tree, unless otherwise specified.

## Service Capabilities and Limits
- 

The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at[support.oracle.com](http://support.oracle.com/).
- 

Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see[Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
- Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Zone Tasks

You can perform the following tasks with zones:
- [Creating a Public DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/gettingstarted_topic-Creating_a_Zone.htm)
- [Creating a Private DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm)
- [Creating a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm)
- [Delegating a Public DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/gettingstarted_topic-Delegating_Your_Zone.htm)
- [Adding Downstream Servers to a Primary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm)
- [Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm)
- [Getting a DNS Zone's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-get.htm)
- [Moving a DNS Zone Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm)
- [Updating a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm)
- [Adding a TSIG Key to a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-tsig-key-to-zone.htm)
- [Deleting a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm)
- [Formatting a DNS Zone File](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/formattingzonefile.htm)
