# Creating a Private DNS Zone in a Private View
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm
- Fetched: 2026-09-05 01:59 CDT

# Creating a Private DNS Zone in a Private View

Create a private domain name service (DNS) zone in a private view to manage records and hostname resolution for applications running within and between virtual cloud networks (VCNs), and on-premises or other private networks.
Private DNS also provides DNS resolution across networks (for example, another VCN within the same region, cross region, or an external network). See[Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm)and[Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/views.htm)for a feature overview and more information.

For general service information, see the[DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).
Note  
  

- Private zones can be viewed only in the region in which they're created.
- You can't create a private zone at or under`oraclevcn.com`within the default protected view of a VCN dedicated resolver.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm#)
- 

- On the Private views list page, select the private view you want to work with. If you need help finding the list page, see[Listing Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-list.htm#top).
- Select the Private zones tab.
- Select Create zone .

Note  
  
The Zone type is set to`Primary`and is read-only.
- Enter a descriptive name for the zone. Avoid entering confidential information.
- Select a compartment to create the zone in.
- Select Create .
- 

Use the[zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html)command and required parameters to create a private zone in a specified private view:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm). sd
- 

Run the[CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)operation to create a private zone in a specified private view.

Specify the zone`scope`as`PRIVATE`. Include the`viewId`parameter, populated with the OCID of the view you want to create the zone in.

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)
