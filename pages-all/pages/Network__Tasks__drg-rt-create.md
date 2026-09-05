# Creating a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm
- Fetched: 2026-09-05 02:44 CDT

# Creating a DRG Route Table

Create a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.

When you create a DRG, two default route tables are created for you: one for VCN attachments and one for all other attachment types. You can[assign a new DRG route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm)to a DRG attachment to change the routing behavior for that attachment.

For details about DRG routing, see[Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- Select Create DRG route table .
- (Optional) Enter a descriptive name for the route table. Avoid entering confidential information.
- (Optional) Under Static route rules , specify a destination for the route table. The route table must include at least one destination, but you can specify more if needed.

- Destination CIDR block: Enter a destination CIDR block, enable import route distribution, or enter nothing and the default CIDR 0.0.0.0/0 is applied which allows all traffic.
- Next hop attachment type: Select the intended target attachment type for the static rule. The attachment type can be Virtual Cloud Network , Remote peering connection , or Cross-tenancy attachment to a VCN.
- Next hop attachment: Select a specific attachment of the selected type as the next hop for this static route rule.
- (Optional) Select Show Advanced options (when present), and make the following selections:

- Enable import route distribution: Select this option to assign an[import route distribution](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__dr_import)to the route table so it dynamically learns new routes based on BGP advertisements.
- Enable ECMP: Select this option to enable equal-cost multi-path routing (ECMP), which disambiguates routing decisions when the same destination can be reached from several paths. See[ECMP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__ecmp)and[Route Conflicts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__conflicts)for more detail on how ECMP works in a DRG.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create DRG route table .

The route table is created and displayed in the DRG route tables area of the DRG details page.
- 

Use the[network drg-route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/create.html)command and required parameters to create a DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/CreateDrgRouteTable)
