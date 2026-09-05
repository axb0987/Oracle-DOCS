# Adding Static Route Rules to a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm
- Fetched: 2026-09-05 02:44 CDT

# Adding Static Route Rules to a DRG Route Table

Add one or more static route rules to a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.

A DRG route rule is a mapping between a destination IP address range (CIDR block) and a DRG attachment. The map is used to route packets that match the rule or rules. Traffic can be routed across the attachments using equal-cost multipath routing ([ECMP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__ecmp)) if several rules have identical destinations and none of the rules[conflict](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__conflicts).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- Select the name of the DRG route table that you want to add a static route rule to.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Static route rules tab.
- Under Resources , select Static route rules .
- Select Add static route rules .
- Enter the following information fro each rule:

- Destination CIDR block: Enter a destination CIDR block, enable import route distribution, or enter nothing and the default CIDR block 0.0.0.0/0 is applied, allowing all traffic. The route table must always include at least one destination.
- Next hop attachment type: Select the intended target type of the static rule.
- Next hop attachment: Select a VCN, cross-tenancy, or remote peering connection (RPC) attachment.
- Select +Another route rule to add more rules.
- Select Add route rules when finished.
- 

Use the[network drg-route-rule add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/add.html)command and required parameters to add one or more static route rules to the specified DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/AddDrgRouteRules)
