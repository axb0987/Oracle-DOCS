# Viewing a Subnet Topology Map
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-subnet-topology-map.htm
- Fetched: 2026-09-05 02:47 CDT

# Viewing a Subnet Topology Map

Use Network Visualizer to view a map that shows a visual representation of the topology of a subnet.

The subnet map provides resource information about the instances, Load Balancer, file storage, and Kubernetes Engine clusters in a subnet. Whether you want to view the resources in the subnet or details about a specific resource, this map provides the flexibility to achieve that. The search capability using name, IP address, or OCID helps you find a resource and quickly get to the resource page.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-subnet-topology-map.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-subnet-topology-map.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-subnet-topology-map.htm#)
- 

- Open the navigation menu and select Networking . Under Network Command Center, select Network visualizer . Wait briefly for the network map to generate.
- Confirm that you're viewing the region and compartment that contain the subnet that you want to see represented in a map. If you need to, select a different compartment. To see resources in all compartments nested within the selected compartment, select Include child compartments .
- In the map, select the virtual cloud network (VCN) that contains the subnet for which you want to view the topology.
- In the Resource summary area, select either View VCN routing map or View VCN security map . While viewing one of these maps, you can easily switch to the other map by selecting the Map Mode option.
- In the map, select the subnet for which you want to view the topology.
- In the Resource summary area, select either View subnet inventory map or View subnet security map . While viewing one of these maps, you can easily switch to the other map by selecting the Map Mode option.
- Select any resource on the map (the resource changes color to indicate the selection) to view basic information for that item in the Resource summary area to the right side of the map. The details presented vary depending on the component that you selected.

The following elements appear in the control bar above the main map area, from leftmost to rightmost:
- Map : Displays the selected subnet.
- Search bar : To find a resource by name, enter the name in the search bar. When a match is found and selected, the view in the main map area zooms in to show that resource.
- Refresh : Updates the view in the main map area. The view is refreshed every three minutes, but if a change was made since the last refresh, you can manually trigger a refresh of the map.
- Filter : Displays the filters used in the current view. You can turn them on and off as needed.
- Export Map Data : Exports a zip file that contains a high-resolution PNG map of the resources in the current subnet, and a PDF file that contains a lower-resolution version of the map plus resource data (such as route tables). The PDF includes only the resource information for the elements shown in the map at the time of export.
- Map Legend : Displays the symbols used in the map and their meaning.
Tip  
  

To navigate back to the regional or VCN topology map, select the name of the region or VCN in the control bar.
- 

Use the[subnet-topology get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet-topology/get.html)command and required parameters to get a virtual network topology for a subnet in the current region and specified compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSubnetTopology](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SubnetTopology/GetSubnetTopology)operation to get a virtual subnet topology for the current region and specified compartment.
The response body contains a single[SubnetTopology](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SubnetTopology/)resource, which contains the following resources showing relationships between entities in the subnet:
- [TopologyEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyEntityRelationship)
- [TopologyContainsEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyContainsEntityRelationship)
- [TopologyAssociatedWithEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyAssociatedWithEntityRelationship)
