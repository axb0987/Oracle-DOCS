# Viewing IP Address Insights
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm
- Fetched: 2026-09-05 02:41 CDT

# Viewing IP Address Insights

Access IP Address Insights to view the IP addresses used across a tenancy in a compartment and get a hierarchical visibility into VCNs, respective subnets, and network resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select IP Address Insights .
- To display the IP Address Insights of a certain region, select a region from the Region menu at the top of the Console.
- To display the IP address insights along with VCNs, respective subnets, and network resources from a specific compartment or many compartments, follow these steps:

- 
- Next to Applied filters , select the Compartments filter.
- Select the compartments that you want to get IP address insights from.
- Select Apply filter .
- Use the Search and Filter box to further refine the search:

- To search resources in IP Address Insights:
- Select the Resource filter.
- Enter a search text to retrieve all resources matching the search text in the IP Address Insights.
- Select Apply Filter . The results matching the search text are listed. For example, if you use the search text 10.0.0.0 , the results include all the resource names and IP addresses matching the search text.

- To display the IP address insights of all resources according to their IP address type, select the Address type filter, select the preferred IP address types, and then apply the filter.
- To display the IP utilization of a particular utilization threshold, select a value from the Utilization greater than or equal to filter, select a value, and then apply the filter.
You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources with the following information:
- Resource : Displays the resource names in a hierarchical order. For example, VCNs, respective subnets, and network resources from a specific compartment or many compartments in a hierarchy. To access the resource details page, select the name of the resource.
- Resource type : Displays the type of resource, for example, VCN.
- CIDR/Prefix/IP : Displays the CIDR block, prefix, or the IP address assigned to the resource.
- Utilization : Displays the IP utilization of the CIDR/prefix associated with a VCN or subnet.
- Overlaps : Displays when the same CIDR/prefix/IP addresses are used by other resources, indicating an overlap. To view the overlaps, select the Actions menu (three dots) (three dots) for the resource and select View overlaps .
- DNS Domain and Host Names : Displays the DNS hostname of the resource. To copy the DNS domain and host names, select the Actions menu (three dots) (three dots) for the resource and select Copy DNS domain &amp; host names .
- Compartment : Displays the compartments where the resources reside. For example, if a VCN is in one compartment and its subnets are in another compartment, all the compartments are listed here.
- 

Use the`network ipam list-ip-inventory`command and required parameters to view the IP addresses used across a tenancy in a compartment:

```

```

Use the`network ipam get-vcn-overlap`command to view the CIDR overlap information of the specified VCN in selected compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Run the`ListIpInventory`operation to view the IP addresses used across a tenancy in a compartment.

Run the`GetVcnOverlap`
