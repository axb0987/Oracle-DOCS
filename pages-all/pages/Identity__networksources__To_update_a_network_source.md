# Updating a Network Source
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networksources/To_update_a_network_source.htm
- Fetched: 2026-09-05 02:25 CDT

# Updating a Network Source

Update a network source in IAM to change the set of IP ranges from which users can sign in.
- On the Network Sources list page, find the network source in the list and select its name to view its details. If you need help finding the network sources list page, see[Listing Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/networksources/listing-networksources.htm#enter-topic-id).
- To edit the description of the network source, select Edit , enter a new description, and select Save Changes .
- To add more allowed IP addresses to this network source, under Networks , select Add Networks . In the Add Networks panel, specify a network as follows, and then select Update :
- Virtual Cloud Network: Select this option and enter the following information:
- 

Select VCN: Choose the VCN that you want to allow. If needed, select Change Compartment to find a VCN in a different compartment.
- 

IP Address/CIDR Block: Enter an IP address from the VCN or a subnet CIDR block. For example: 10.0.0.0/16 or 10.0.0.4.

To allow all subnets from the specified VCN, enter 0.0.0.0/0.

Select + Another IP Address/CIDR Block to add another allowed address or range from the same VCN
- Public Network: Select IP Address/CIDR Block and enter a specific IP address or CIDR block range. For example: 192.0.2.143.

Select + Another IP Address/CIDR Block to add another allowed address or range.
-
