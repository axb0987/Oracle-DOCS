# Creating a VCN Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a VCN Route Table

Create a Virtual Cloud Network (VCN) route table in a specific VCN and compartment.
For an overview of routing in VCNs and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Routing tab.
- Under Resources , select Route Tables .
- Select Create Route Table .
- Enter a friendly name for the route table. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the route table in. Select another compartment if needed.
- (Optional) Select +Additional Route Rule to add one or more route rules, each with the following information. You can create a route table with no rules and then add them later.

- Target Type: See the list of target types in[Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN). If the target type is a DRG , the VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. If the target is a private IP object, before you specify the target you must first disable the source/destination check on the VNIC that uses that private IP object. For more information, see[Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/managingroutetables.htm#Route).
- Destination CIDR Block : Available only if the target isn't a[service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/servicegateway.htm). The value is the destination CIDR block for the traffic. You can provide a specific destination CIDR block, or use 0.0.0.0/0 if all traffic leaving the subnet needs to be routed to the target specified in this rule.
- Destination Service: Available only if the target is a[service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/servicegateway.htm). The value is the[service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/servicegateway.htm#overview)that you're interested in.
- Compartment: The compartment containing the target.
- Target: The target. If the target is a private IP object, enter its OCID. Or you can enter the private IP address itself, in which case the Console finds the corresponding OCID and uses it as the target for the route rule.
- Description: An optional description of the rule.
- (Optional) Select Show Tagging Options and assign tags to the route table.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
The route table is created and then displayed on the Route Tables list. You can now specify this route table when creating or updating a subnet.
- 

Use the[network route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/create.html)command and required parameters to create a VCN route table:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable)
