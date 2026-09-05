# Adding a Record to a DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm
- Fetched: 2026-09-05 01:59 CDT

# Adding a Record to a DNS Zone

Add records that contain domain information to a domain name service (DNS) zone. Each record type contains information called record data (RDATA).

For example, the RDATA of an[A](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_a-record)or[AAAA](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_aaaa)record contains an IP address for a domain name, while MX records contain information about the mail server for a domain. Oracle Cloud Infrastructure normalizes all RDATA into the most machine-readable format. The returned presentation of RDATA might differ from its initial input. For more information, see[Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm).

For general service information, see the[DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm)
Note  
  
You can't manage records when a zone isn't active.
- If the zone is updating, wait a few moments and try again.
- If the zone is in a failed state, delete the zone and re-create it. Be sure the zone name is unique, and that no error exists in any zone file you might have used to create the zone.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#)
- 

Note  
  
The number and type of records in a zone depend on the goals for the zone and its DNS management.

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Tasks/zone-list.htm#top).
- Select the Records tab.

A list of records appear. Records that have the same name, type, and TTL are displayed as a single RRset in the Zone Records list.
- Select Manage records .
- Select Add record .
- In the Add record panel, enter record information:
- (Optional) Enter a Name for the record. Avoid entering confidential information.
- Select a record Type . For more information about record types, see[Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm).
- Enter a TTL (time to live) for the record.
- In the RDATA/Answers section, select the RDATA entry mode and then enter the record information:

- Select Basic to enter one record at a time. Select +Another record to add more records.
- Select the switch to select Advanced and add many records at the same time. Each record must be on its own line.
- Select Add record .
- Select Publish changes .
- On the Confirm page, review the changes, and then select Confirm publish changes .
- 

Important  
  

- If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
- When the zone name is provided as a path parameter and PRIVATE is used for the scope query parameter, then the`viewId`query parameter is required.
- 

Use the[record rrset update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/update.html)command and required parameters to add a single record in an RRset in a zone. An RRset is defined as a group of records that have the same name, type, and TTL values.

```

```

- 

Use the[record zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/zone/update.html)command and required parameters to bulk add records to a zone.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Important  
  

- If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
- When the zone name is provided as a path parameter and PRIVATE is used for the scope query parameter then the`viewId`query parameter is required.

- 

Run the[UpdateRrset](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/UpdateRRSet)operation to add a single record to an RRset in a zone. An RRset is defined as a group of records that have the same name, type, and TTL values.
- 

Run the[UpdateZoneRecords](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/UpdateZoneRecords)
