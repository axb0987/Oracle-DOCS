# Viewing IP Address Insights of a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_subnet_details.htm
- Fetched: 2026-09-05 02:41 CDT

# Viewing IP Address Insights of a Subnet

View the IP addresses used by a subnet in a tenancy, and the list of IP resources within a subnet, by accessing IP Address Insights of a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_subnet_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_subnet_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_subnet_details.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select IP Address Insights .
- Use filters to refine the search. You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources. For more information about the available filters, see[Viewing IP Address Insights](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm).
- Expand the name of the VCN that contains the subnet.
- Select the name of the subnet to open the subnet details page.
- Select the IP administration tab.
- In the IP Address Insights section, view the list of IP addresses used in the subnet along with the details of the associated resources along with following information:

- 
- DNS hostname : Displays the DNS hostname of the subnet.
- IP address : Displays the IP address assigned to the subnet.
- CIDR/prefix : Displays the assigned CIDR block or prefix.
- Associated public IP : Displays the assigned public IP address of the subnet.
- Public IP lifetime : Displays the type of IP address, which is either Ephemeral or Reserved . For more information, see[Types of Public IPs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph).
- Associated public IP pool : Displays the IP pool from which the public IP is assigned to the subnet.
- Address type : Displays the type of IP address assigned to the subnet.
- Assigned : Displays the date and time when the IP address was assigned to the subnet.
- 

Use the`network ipam get-subnet-inventory`command and required parameters to view the IP addresses and resources used within a subnet in a tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Run the`GetSubnetIpInventory`
