# Reserved IP Addresses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-ipv6.htm
- Fetched: 2026-09-05 02:46 CDT

# Reserved IP Addresses

Reserve IP addresses to control IP address allocation by taking them out of the dynamic allocation pool and prevent them from being used for automatic allocations. Use reserved IP addresses to statically allocate IP addresses within a VCN.

When resources assigned with reserved IP addresses are rebooted or redeployed, they retain their assigned reserved IP addresses and ensure uninterrupted services. To assign public IP addresses to reserved private IPv4 addresses, edit the private IP address assigned to the compute VNIC. For more information, see[Assigning a Reserved Public IP to a Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm).
The following management actions are available for IP addresses of all resources in a subnet:
- [Reserved IPv4 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-addresses.htm)
- [Reserved IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-addresses.htm)

For information about the list of all IP addresses used within a subnet, including ephemeral, reserved public, reserved private, and reserved IPv6 addresses, see[IP Address Insights](https://docs.oracle.com/iaas/Content/Network/Concepts/ip_inventory.htm)
