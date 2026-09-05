# Reverse DNS
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm
- Fetched: 2026-09-05 01:59 CDT

# Reverse DNS

Reverse DNS maps an IP address to a hostname .

The reverse domain name service (rDNS) serves several different purposes from email to network troubleshooting. Some benefits include:
- Adding a label for network troubleshooting tools such as traceroute.
- Populating the "Received:" header field in an SMTP email.
- Checking for generic reverse DNS such as`1-2-3-4.example.com`to identify spammers.
- Verifying a relationship between the owner of a domain name and the owner of the server (IP address).
- Writing a human readable hostname to the log files for system monitoring tools.
- Evaluating which hostname is affected when maintenance is performed on an IP address.

Note  
  
You can only create reverse DNS zones for IP ranges that you control.[Contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm#Contacti)to request a reverse DNS ([PTR](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_ptr)) record for an IP address owned by Oracle. For example, a public IP address that was automatically assigned to a Compute instance or Load Balancer. For more information, see[Reverse DNS (PTR)](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm#reverse_dns).

Before getting started with setting up reverse DNS within an Oracle Cloud Infrastructure account, contact the IP provider and confirm that they support delegation of reverse DNS zone . If they don't support delegation, typically they can host a pointer record (PTR) for you and no reverse DNS configurations are required within the OCI account. If they do support delegation, confirm the exact syntax of the reverse DNS hostname with them, as some providers use slashes and some use dashes. Also, if you're delegating a reverse DNS zone, confirm that this zone matches exactly what you configure in the OCI account as this is necessary for delegation to work.

After you create and publish a reverse DNS zone and PTR records, you can update the reverse DNS zone delegation with the IP provider. Delegation changes aren't required with the domain registrar with a reverse DNS zone.

Setting up a reverse DNS zone is different for the two types of IP address blocks. Use the following procedures to set up a reverse DNS zone for a IP address block type.

## Setting Up Reverse DNS for Classless Address Block (Partial Range of IP Addresses)

[To find a reverse DNS zone name using classless address block](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

- Make a note of the network IP address. For example,`192.168.15.224/27`.
- Remove the netmask part of the address. This is the number after the slash (/). For example, remove the`27`after the IP address,`192.168.15.224/27`.
- Reverse the order of the remaining octets. For example,`224.15.168.192`.
- 

Append`in-addr.arpa`to the end of the IP address. For example,`224.15.168.192.in-addr.arpa`.
Note  
  

Some assigning authorities require you to use a slash (/) instead of a dash (-) in the reverse address. Ask which character to use when you contact the assigning authority to delegate the reverse address.
- Add the netmask back into the address. For example,`224-27.15.168.192.in-addr.arpa`.

In this example,`224-27.15.168.192.in-addr.arpa`is the reverse DNS zone name.

[To create a DNS zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- Select Create zone .
- Select a Method for creating the zone.
- If you select the Manual method, enter the following information:
- Zone Name: Enter the name of a zone you want to create. Avoid entering confidential information.
- Create in Compartment: Specify the compartment you want to create the zone in. Be sure you have permission to work in the compartment.
- Zone Type: To control the zone contents directly within OCI, select Primary . If you want OCI to pull zone contents from an external server, select Secondary and enter a Zone Master Server IP address.
- If you select the Import method:
- Drag, select, or paste a valid zone file into the Import Zone File window. The zone is imported as a primary zone. For information about formatting a zone file or how to change a zone file exported from`GoDaddy.com`, see[Formatting a DNS Zone File](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/formattingzonefile.htm).
- Select Create .

The system creates and publishes the zone, complete with the necessary SOA and NS records.

[To create a pointer record (PTR) for each host address](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

As part of the process of setting up a reverse DNS zone, you need to add a[PTR](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_ptr)record for each host address. This ensures requests are correctly routed for resolution.
- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- 

Select the Zone Name in which you want to add the PTR record. Zone details appear.
Tip  
  
You can use the Zone Name sort filter to list to sort zone names alphanumerically in ascending or descending order.
- Select Records . A list of zone records appear.
- Select Add Record .
- 

In the Add Record dialog box, select the PTR – Pointer record type from the list. Enter the following information:
- Name: Optional. Name of the subdomain.
- TTL: Select the lock icon to unlock this field. All PTR records in the zone are updated to reflect the last changes to TTL. This value indicates how long you want to use external nameservers to cache the information about a DNS record.
- TTL Unit: Select the unit of time used for the TTL value.
- RData Mode: Select Basic or Advanced format. If you select Advanced, enter the canonical hostname (for example,`example.com`) that the record is going to point to in the RDATA field.
- Hostname: The web address of the zone.

For more information about the PTR record type, see[Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm).
- Select Submit .
- After the record is added, select Publish Changes .
- 

In the confirmation dialog box, select Publish Changes .

[To add CNAME records for each host at the ISP](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

If the IP provider doesn't automatically configure the[CNAME](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_cname)record on your behalf, you need to add a CNAME record for each host at the ISP. This is done to ensure requests are correctly routed for resolution.
- Make a note of the IP address and the preferable CNAME for each host in the new reverse DNS zone.
- Contact the ISP and request that they append a CNAME record for each host in the Oracle Cloud Infrastructure DNS zone to your account with them.
- 

Test the reverse DNS path by running the following command:

```

```

See[Testing DNS Using dig](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm)for more information.

The returned information shows that the reverse domain is now being resolved.

[To update zone delegation](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

To make the OCI hosted zone accessible through the internet, you must delegate the domain with the domain's registrar (This is the website where you bought the domain, such as`GoDaddy.com`or`Bluehost.com`).
- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- Select the Zone Name for the zone you want to delegate. Zone details and a list of records appear.
- Use the Type sort filter to find the NS records for the zone.
- Note the name servers in the RDATA field within each NS record.

You can use the noted name servers to change the domain's DNS delegation. See the registrar's documentation for instructions.

#### Setting Up Reverse DNS for Full Address Block

## Setting Up Reverse DNS for Full Address Block

[To find a reverse DNS zone name using full address block](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

- Make a note of the network IP address. For example, 192.168.15.0 .
- Remove the netmask part of the address (the last number in the set of 4). For example, 192.168.15 .
- Reverse the order of the remaining three octets. For example, 15.168.192 .
- Append ' in-addr.arpa ' to the end. For example, 15.168.192.in-addr.arpa

In this example, 15.168.192.in-addr.arpa is the reverse DNS zone name.

[To create a DNS zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- Select Create Zone .
- Select a Method for creating the zone.
- If you select the Manual method, enter the following information:
- Zone Name: Enter the name of a zone you want to create. Avoid entering confidential information.
- Create in Compartment: Specify the compartment you want to create the zone in. Be sure you have permission to work in the compartment.
- Zone Type: To control the zone contents directly within OCI, select Primary . If you want OCI to pull zone contents from an external server, select Secondary and enter a Zone Master Server IP address.
- If you select the Import method:
- Drag, select, or paste a valid zone file into the Import Zone File window. The zone is imported as a primary zone. For information about formatting a zone file or how to change a zone file exported from`GoDaddy.com`, see[Formatting a DNS Zone File](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/formattingzonefile.htm).
- Select Create .

The system creates and publishes the zone, complete with the necessary SOA and NS records.

[To create a pointer record (PTR) for each host address](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

As part of the process of setting up a reverse DNS zone, you need to add a PTR record for each host address. This is done to ensure requests are correctly routed for resolution.
- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- 

Select the Zone Name in which you want to add the PTR record. Zone details appear.
Tip  
  
You can use the Zone Name sort filter to list to sort zone names alphanumerically in ascending or descending order.
- Select Records . A list of zone records appear.
- Select Add Record .
- 

In the Add Record dialog box, select the PTR – Pointer record type from the list. Enter the following information:
- Name: Optional. Name of the subdomain.
- TTL: Select the lock icon to unlock this field. All PTR records in the zone are updated to reflect the last changes to TTL. This value indicates how long you want to use external nameservers to cache the information about a DNS record.
- TTL Unit: Select the unit of time used for the TTL value.
- RData Mode: Select Basic or Advanced format. If you select Advanced, enter the canonical hostname (for example,`example.com`) that the record is going to point to in the RDATA field.
- Hostname: The web address of the zone.

For more information about the PTR record type, see[Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm).
- Select Submit .
- After the record is added, select Publish Changes .
- 

In the confirmation dialog box, select Publish Changes .

[To update zone delegation](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#)

To make the OCI hosted zone accessible through the internet, you must delegate the domain with the domain's registrar.
- Open the navigation menu and select Networking . Under DNS management , select Overview .
- Select Zones .
- Select the Zone Name for the zone you want to delegate. Zone details and a list of records appear.
- Use the Type sort filter to find the NS records for the zone.
- Note the name servers in the RDATA field within each NS record.
