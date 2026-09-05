# Viewing CIDR or Prefix Utilization of a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm
- Fetched: 2026-09-05 02:41 CDT

# Viewing CIDR or Prefix Utilization of a Subnet

View the percentage of IP addresses used from an IPv4 CIDR block or IPv6 prefix assigned to a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select IP Address Insights .
- Use filters to refine the search. You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources. For more information about the available filters, see[Viewing IP Address Insights](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm)
- Expand the name of the VCN that contains the subnet.
- Select the name of the subnet to open the subnet details page.
- Select the IP administration tab.
- Under Resources , select CIDR/Prefix utilization .
- In the CIDR/Prefix utilization section, view the list of IPv4 CIDR blocks and IPv6 prefixes the subnet uses along with the percentage of IPs used from the CIDR block or prefix assigned to the subnet.
- 

Use the`network ipam get-subnet-cidr-utilization`command and required parameters to view the percentage of IP addresses used from an IPv4 CIDR block or IPv6 prefix assigned to a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Run the`GetSubnetCidrUtilization`
