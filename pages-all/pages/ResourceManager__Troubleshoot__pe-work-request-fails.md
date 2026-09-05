# Private Endpoint Work Request Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/pe-work-request-fails.htm
- Fetched: 2026-09-05 02:57 CDT

# Private Endpoint Work Request Fails

Troubleshoot a failed work request for a private endpoint.

When you[create a private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-private-endpoints.htm), the work request for the creation operation fails.

One possible cause of a failed work request for creating a private endpoint is lack of IP addresses in the specified subnet. This situation can occur when the specified subnet is configured for a small CIDR block of IP addresses, and all IP addresses in that block are already used.

To remedy this issue, you can resize the VCN and try again, or select a different subnet that has enough IP addresses.

For more information, see[Changing a VCN's IPv4 CIDR blocks](https://docs.oracle.com/iaas/Content/Network/Tasks/edit_vcn_cidr.htm)and[IP Address Insights](https://docs.oracle.com/iaas/Content/Network/Concepts/ip_inventory.htm)
