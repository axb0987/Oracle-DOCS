# Formatting a DNS Zone File
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm
- Fetched: 2026-09-05 01:58 CDT

# Formatting a DNS Zone File

A domain name service (DNS) zone file is a text file that describes a DNS zone . The BIND file format is the industry preferred zone file format and has been widely adopted by DNS server software.

The format is defined in[RFC 1035](https://tools.ietf.org/html/rfc1035).

## Zone File Limitations and Considerations

### Service Limits

The Oracle Cloud Infrastructure DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at[support.oracle.com](http://support.oracle.com/).

### Zone File Limits

Zone file uploads are limited to 1 megabyte (MB) in size per zone file.

To work around this limitation, first use either the[console](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/../Tasks/managingdnszones.htm)or the[`CreateZone`](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)API operation to create a zone. Then, use the[`PatchDomainRecords`](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/PatchDomainRecords)API operation to add records to the zone in batches of 100.

### Import and Export Limits

Exporting zone files containing ALIAS record types or that use Traffic Management (TM) isn't supported. This is because zone files are exported as RFC standard records, and ALIAS records and TM are nonstandard record types. You can use the[`GetZoneRecords`](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/GetZoneRecords)API operation to obtain a backup of nonstandard records. Use the`limit`parameter to create batches of 100 records each.

Import and export for global zones is supported in both the Console and API, except for[ALIAS](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_alias)and TM records.

For private zones, import is supported using the[`CreateZone`](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)API operation. Zone export isn't supported.

## Example of a Zone File

This is an example of a zone file downloaded from Oracle Cloud Infrastructure DNS.
```

```

Note  
  

Record Classes

In the preceding example zone file, no record classes are displayed. OCI DNS only works with Internet (IN) class records but omits the class information in zone files for efficiency purposes.

## Anatomy of a Zone File

`$ORIGIN`indicates a DNS node tree and typically starts a DNS zone file. Any host labels following the origin append the origin hostname to assemble a fully qualified hostname. Any host label within a record that uses a fully qualified domain name ending with a period isn't append the origin hostname.

Example: With`ORIGIN example.com.`, any record where the host label field isn't followed by a period,`example.com`. is appended to them.

The "@" symbol is a special label that indicates the`$ORIGIN`needs to replace the "@" symbol. This is typically used for the apex of a zone.

SOA Record – The`$ORIGIN`is followed by the zone's Start Of Authority (SOA) record. An SOA record is required for each zone. It contains the name of the zone, the e-mail address of the party responsible for administering the domain's zone file, the current serial number of the zone, the primary nameserver of the zone, and various timing elements (measured in seconds).

### SOA Record Format

```

```

- Primary Name Server – The nameserver that contains the original zone file and not an AXFR transferred copy.
- Hostmaster Email – Address of the party responsible for the zone. A period "." is used in place of an "@" symbol. For email addresses that contain periods, replace the periods with a slash "/".
- Serial Number – Version number of the zone. The serial number increases with each following update to the zone.
- Time To Refresh – How long a nameserver waits before checking for a serial number increase within the primary zone file, in seconds. An increased serial number detected by a secondary DNS nameserver means a transfer is needed to sync the records. Only applies to zones using secondary DNS.
- Time To Retry – How long a nameserver waits before retrying to update a zone after a failed try, in seconds. Only applies to zones using secondary DNS.
- Time To Expire – How long a nameserver waits before considering data from a secondary zone invalid and to stop answering queries for that zone, in seconds. Only applies to zones using secondary DNS.
- Minimum TTL – Minimum Time To Live (TTL). How long a nameserver or resolver caches a negative response, in seconds.

## Anatomy of a Record Within a Zone File

A zone file is a collection of resource records with each record entry described in the following sequence:

Format: Host Label TTL Record Class Record Type Record Data
Example: example.com. 60 IN A 104.255.228.125
- Host Label – A host label helps to define the hostname of a record and whether the`$ORIGIN`hostname is appended to the label. Fully qualified hostnames terminated by a period aren't append the origin.
- TTL – The Time To Live (TTL) is the amount of time that a DNS record is cached by an outside DNS server or resolver, in seconds.
- Record Class – Three classes of DNS records exist: IN (Internet), CH (Chaosnet), and HS (Hesiod). Oracle Cloud Infrastructure DNS only uses the IN class of records.
- Record Type – The type of a record, such as CNAME, AAAA, or TXT.
- Record Data – The data within a DNS answer, such as an IP address, hostname, or other information. Different record types contain different types of record data.

## Amending Zone Files Exported from GoDaddy for Import

GoDaddy.com exports zone files in a proprietary format. To get the OCI DNS service to correctly import a zone file exported from GoDaddy, you must directly alter the file. Follow these instructions to update the zone file.
- Export the zone file from GoDaddy. Reference GoDaddy's documentation to see how this is done.
- Open the file in any preferred text editor.
- Prepend a new line to the file before the SOA record with the following information, including the trailing period:`$ORIGIN [yourdomain].`
- After the file has been amended, save the changes to the file and use the zone import function to import the file into the DNS configuration. For more information about zone import, see[Managing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/../Tasks/managingdnszones.htm).
Note  
  
If the zone file includes includes dynamic A records, such as`@ 600 IN A GoCentral Published Site`, you need to amend these records with the correct IP addresses of the website. Contact GoDaddy for information about how to obtain this information. Example:`@ 600 IN A 192.0.2.255`

Example:

This is an example of a zone file exported from GoDaddy. The code in bold is the code that needs to be removed from the file for it to be eligible for import into Oracle Cloud Infrastructure DNS.
Tip  
  
Placing a semicolon at the beginning of a line is valid comment syntax for a zone file per[RFC 1035](https://tools.ietf.org/html/rfc1035#section-5.1), but for ease of use and formatting we recommend removing the large section of comments from the beginning of the zone file provided by GoDaddy, as shown.
```

```

The following example shows an amended zone file ready to import into OCI DNS. The code in bold needs to be prepended to the zone file before import.
```

```
